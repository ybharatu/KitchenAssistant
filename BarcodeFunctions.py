import cv2
import numpy as np
import pyzbar
import matplotlib
#matplotlib.use('PS')
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import copy
from PIL import Image
import getopt
import sys

# Global Variables
buffer_val = 10

# Function to find barcode from image
def find_barcode( img ):

    cv2.imshow("Colored Image", img)
    # Grayscale Image
    gray1 = convert_gray( img )
    #plt.title('Image 1')
    #plt.imshow(gray1, cmap='gray')
    #plt.show()

    # Test between Sobel and Scharr Operator
    gradXSobel = cv2.Sobel(gray1, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradYSobel = cv2.Sobel(gray1, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
    gradXScharr = cv2.Scharr(gray1, ddepth=cv2.CV_32F, dx=1, dy=0)
    gradYScharr = cv2.Scharr(gray1, ddepth=cv2.CV_32F, dx=0, dy=1)

    # Gradient Detection
    gradientSobel = cv2.subtract(gradXSobel, gradYSobel)
    #gradientSobel = cv2.convertScaleAbs(gradientSobel)
    gradientScharr = cv2.subtract(gradXScharr, gradYScharr)
    #gradientScharr = cv2.convertScaleAbs(gradientScharr)

    # Add Blur
    blurredSobel = cv2.blur(gradientSobel, (1, 1))
    cv2.imshow("Blurred Sobel",blurredSobel)
    blurredScharr = cv2.blur(gradientScharr,(4,4))
    #cv2.imshow("Blurred Scharr", blurredScharr)

    # Assign pixel to be balck if value <255
    ret, threshSobel = cv2.threshold(blurredSobel, 2, 255, cv2.THRESH_BINARY)
    cv2.imshow("thresh Sobel", threshSobel)
    ret, threshScharr = cv2.threshold(blurredScharr, 2, 255, cv2.THRESH_BINARY)
    #cv2.imshow("thresh Scharr", threshScharr)

    # Applies Canny Edge detection on the grayscale image (UNNECESSARY)
    cannySobel = cv2.Canny(threshSobel.astype(np.uint8),2,255)
    cannyScharr = cv2.Canny(threshScharr.astype(np.uint8),2,255)
    cv2.imshow("Canny Sobel", cannySobel)
    #cv2.imshow("Canny Scharr", cannyScharr)

    # Hough Line Transform Function
    HoughSobel = hough_line(threshSobel.astype(np.uint8), img)
    #HoughScharr = hough_line(threshScharr)
    x_dist = find_groups(HoughSobel)

    # Using X values plus BUFFER value, set all pixels to black outside x range
    maskSobel = np.zeros(threshSobel.shape,np.uint8)
    maskSobel[0:,x_dist[0]:x_dist[1]] = threshSobel[0:,x_dist[0]:x_dist[1]]
    maskScharr = np.zeros(threshScharr.shape, np.uint8)
    maskScharr[0:, x_dist[0]:x_dist[1]] = threshScharr[0:, x_dist[0]:x_dist[1]]
    cv2.imshow("Mask Sobel", maskSobel)
    #cv2.imshow("Mask Scharr", maskScharr)

    # construct a closing kernel and apply it to the thresholded image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closedSobel = cv2.morphologyEx(maskSobel, cv2.MORPH_CLOSE, kernel)
    closedScharr = cv2.morphologyEx(maskScharr, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closed Sobel Before morph", closedSobel)
    #cv2.imshow("Closed Scharr Before morph", closedScharr)

    # perform a series of erosions and dilations
    closedSobel = cv2.erode(closedSobel, None, iterations=4)
    closedSobel = cv2.dilate(closedSobel, None, iterations=4)
    closedScharr = cv2.erode(closedScharr, None, iterations=4)
    closedScharr = cv2.dilate(closedScharr, None, iterations=4)
    cv2.imshow("Closed Sobel", closedSobel)
    #cv2.imshow("Closed Scharr", closedScharr)

    # Find max and min points of white pixels
    coord_sobel = find_rect(closedSobel)
    left = coord_sobel[0]
    right = coord_sobel[1]
    top = coord_sobel[2]
    bottom = coord_sobel[3]
    newimg = cv2.rectangle(img, (left,top), (right,bottom), (0,0,255),2)
    cv2.imshow("After Mask Sobel", newimg)
    #print(coord_sobel)

    # waits for user to press any key
    # (this is necessary to avoid Python kernel form crashing)
    cv2.waitKey(0)

# Function that finds the highest and lowest white pixel. Returns Rectangle coordinates.
def find_rect( img ):
    bottom = 0
    top = 999999999
    right = 0
    left = 999999999
    # for y in img:
    #     for x in img:
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            #print(str(y), str(x))
            if img[y][x] > 0:
                if y > bottom:
                    bottom = y
                if y < top:
                    top = y
                if x > right:
                    right = x
                if x < left:
                    left = x

    print("Left Most: " + str(left))
    print("Right Most: " + str(right))
    print("Top: " + str(top))
    print("Bottom: " + str(bottom))

    # Left
    # Most: 262
    # Right
    # Most: 167
    # Top: 136
    # Bottom: 43

    return (left - buffer_val,right+buffer_val,bottom+buffer_val,top-buffer_val)


# Function to find groups of vertical lines to narrow range of barcode location
def find_groups ( lines ):
    sort_lines = sorted(lines)
    diffs = []
    groups = []
    cur_group = []
    biggest = []
    started = 0
    prev = 999
    ct = 0

    for i in sort_lines:
        if prev == 999:
            prev = i
        else:
            diffs.append( i - prev)
            prev = i

    for i in diffs:
        if i < 25:
            #print(str(i) + " is < 25 so add " + str(sort_lines[ct]) + " to group")
            cur_group.append(sort_lines[ct])
            if started == 0:
                cur_group.append(sort_lines[ct+1])
                started = 1
                ct = ct + 1
            ct = ct + 1
        else:
            #print(str(i) + " is > 25 so SKIP " + str(sort_lines[ct]))
            if len(cur_group) > 0:
                groups.append(cur_group)
                cur_group = []
            ct = ct + 1
    if len(cur_group) > 0:
        groups.append(cur_group)

    for g in groups:
        if len(biggest) == 0:
            biggest = g
        elif len(g) > len(biggest):
            biggest = g

    minv = min(biggest)
    maxv = max(biggest)

    print("Sorted x values: " + str(sort_lines))
    print("Difference:      " + str(diffs))
    print("Groups:          " + str(groups))
    print ("Big Group:      " + str(biggest))
    print("Min: " + str(minv) + " Max: " + str(maxv))
    return (minv, maxv)

# Function to proform hough line transform and draw the lines onto image
# Returns x coordiantes of each line
def hough_line( img, c_img ):
    lines = cv2.HoughLines( img, 1, np.pi/180, 50)
    new_img = copy.deepcopy(c_img)
    i = 0
    cv2.imshow("Colored Image in Transform", c_img)
    r_lines = []
    for j in lines:
        for rho, theta in j:
            #if (theta * (180/np.pi)) < 5:

                #print("Rho = " + str(rho) + " Theta = " + str(theta * (180/np.pi)))
                #w,x,y,z = j
                #print("X0 = " + str(w) + " Y0 = " + str(x) + " X1 = " + str(y) + " Y1 = " + str(z))
            if (theta * (180/np.pi)) < 5:
                i = i + 1
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
                x1 = int(x0 + 50 * (-b))
                # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
                y1 = int(y0 + 50 * (a))
                # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
                x2 = int(x0 - 50 * (-b))
                # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
                y2 = int(y0 - 50 * (a))

                r_lines.append(x1)
                new_img = cv2.line(new_img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    print ("num horizontal lines = " + str(i))
    cv2.imshow("Hough Line", c_img)
    return r_lines

# Function to grayscale image
def convert_gray( img ):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Main Driving Function
if __name__ == "__main__":

    vid = False
    save = False
    live = False
    im = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv:sli:f:", ["help", "video", "save", "live", "image", "filename="])
        print(opts)
    except getopt.GetoptError:
        print('BarcodeFunctions.py -i <filename>')
        sys.exit(2)

    print("Got here!")
    print(sys.argv)

    #################################################################
    # Parses options
    #################################################################
    for opt, arg in opts:
        print("Got here!")
        print(opt)
        print(arg)
        if opt == '-h':
            print('-v --video: Enables video processing. Usage: python3 lane_detect.py -v <filename>')
            print('-l --live: Enables live video processing. Usage: python3 lane_detect.py -l')
            print('-i --image: Enables still image processing. Usage: python3 lane_detect.py -i <filename>')
            print('-s --save: Saves processed images (Slower Performance).')
            sys.exit()
        elif opt in ("-f", "--filename"):
            filename = arg.strip()
        elif opt in ("-v", "--video"):
            vid = True
            filename = arg.strip()

            print("Video Processing")
        elif opt in ("-l", "--live"):
            live = True
            filename = "livefeed"

            print("Live Processing")
        elif opt in ("-i", "--image"):
            im = True
            filename = arg.strip()

            print("Image Processing")
        elif opt in ("-s", "--save"):
            print("Saving Image")
            save = True

        #################################################################
        # Exits if main option is not set
        #################################################################
        if not vid and not im and not live:
            print("Please specify input type (Video (-v), Image (-i), or Live (-l)")
            sys.exit()

    #img1 = "TestImages/barcode1.png"
    img1 = filename
    image = mpimg.imread(img1)
    find_barcode(image)