from pymongo import MongoClient
from multiprocessing import Process
import time
from datetime import datetime
import smtplib
import storage



# Function that updates an item in the database
def update_item( food, cmd ):
    # Asks name of item to update (TODO: Parse information from initial command and ask remaining info)
    item_name = input("Name: ")

    # Gets appropriate item
    r_item = food.find_one({"name": item_name})

    if r_item is not None:
        # Asks for quantity (TODO: Ask to update other fields)
        quantity = input("Quantity: ")

        if int(quantity) == 0:
            remove_item(food, "remove", item_name)
        else:
            food.update_one({"_id": r_item.get("_id")}, {"$set": {"quantity" : quantity }})
        return 1
    else:
        print("Item " + item_name + " is not in database")
        return 0


# Function that removes an item from the database
def remove_item( food, cmd, item_name="" ):
    # Asks name of item to remove (TODO: Parse information from initial command and ask remaining info)
    if item_name == "":
        item_name = input("Name: ")

    # Creates query to search
    myquery = { "name" : item_name }

    # Gets appropriate item
    r_item = food.find_one({ "name" : item_name})

    if r_item is not None:
        # Removes item
        food.delete_one( { "_id" : r_item.get("_id") })
        return 1
    else:
        print("Item " + item_name + " is not in database")
        return 0


# Function that prints out all items
def print_items( food, cmd ):

    # Iterates through all items in database list and prints
    for item in food.find():
        print(item)


# Function that adds item to database
def add_item( food, cmd ) :

    # Asks information about each item to add (TODO: Parse information from initial command and ask remaining info)
    item_name = input("Name: ")
    quantity = input("Quantity: ")
    expiration_date = input("Expiration Date (Press Enter if N/A): ")

    # Creates entry for list
    item_entry = {
        'name': item_name,
        'quantity': quantity,
        'expire': expiration_date
    }

    # Inserts entry
    food.insert_one(item_entry)

# Multiprocessing function that sends Email Notifications
def EmailNotifyRun ( StillRunning, food ):


    while ( StillRunning ):
        # Code that routinely checks expiration dates

        # Gets today's date as a date object
        today = datetime.today()

        # Iterates through items
        for item in food.find():

            # Gets expiration date and converts to datetime object
            ex_date = item.get("expire")
            ex_d = datetime.strptime(ex_date, '%m/%d/%y')

            # Compare dates
            if( today > ex_d ) :
                #print( item.get("name") + " is expired!")

                # Email Code
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(storage.GMAIL_USER, storage.GMAIL_PASS)
                message = item.get("name") + " Expired"
                s.sendmail("KitchenApp@gmail.com", storage.GMAIL_USER, message)
                s.quit()

        # Only notifies once a day (86400 seconds)
        time.sleep(86400)


# Main Driving Function
if __name__ == "__main__":

    # Varable to signal process 2 to end
    StillRunning = 1

    # Enable Mongo Client
    client = MongoClient('localhost', 27017, connect=False)

    # Create Database
    db = client['Ingredients']

    # Create Database list
    food = db.food

    # Create and start Email Notification Process
    EmailNotifyP = Process(target=EmailNotifyRun, args=(StillRunning,food))
    EmailNotifyP.start()

    while True:
        # Asks user for command and formats for parsing
        cmd = input("Command: ")
        cmd = cmd.strip().lower()

        # Parses command
        if cmd == "add":
            add_item(food, cmd)
        elif cmd == "print" or cmd == "ls":
            print_items(food, cmd)
        elif cmd == "remove":
            remove_item(food, cmd)
        elif cmd == "update":
            update_item(food, cmd)
        elif cmd == "quit" or cmd == "exit" or cmd == "q":
            StillRunning = 0
            break
        else:
            # TODO: Should have a -h or -verbose option
            print("Not a valid command")

    # Ends Email Notify Process TODO: Look into Daemon Processes
    EmailNotifyP.terminate()



