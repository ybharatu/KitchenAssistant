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

# Function that Returns recipes using existing ingredients
def search_recipe_by_ingredients ( food ):

    # Empty comma separated list of ingredients
    ingredients = ""
    # Iterates through all items in database list and concats ingrediants
    for item in food.find():
        ingredients = ingredients + item.get("name") + ","

    # Uses current ingredients to search for recipe. Paramters: ingredients (comma seperated string of ingredients),
    # number (how many recipes), limitLicense (something to due with websites with Licensing),
    # ranking ( 1 = prioritize using all ingredients, 2 = prioritize having less missing ingredients),
    # fillIngredients (not sure, wasn't on documentation)
    response = sp_api.search_recipes_by_ingredients(ingredients=ingredients, number=1, limitLicense=True , ranking=2, fillIngredients=True)

    # Json to array conversion
    data = response.json()

    # Iterates through recipes returned
    for item in data:
        # All ingredients are available: Print out steps and ingredients
        if item['missedIngredientCount'] == 0:
            print("You have everything needed to make " + item['title'])

            # Prints required Ingredients
            print("Ingredients:")
            for ingred in item['usedIngredients']:
                print(str(ingred['amount']) + " " + ingred['unit'] + " " + ingred['name'])

            # Finds instructions and prints them step by step
            instr = sp_api.get_analyzed_recipe_instructions(id=item["id"],stepBreakdown=True)
            instr_data = instr.json()
            for step in instr_data[0]['steps']:
                print("Step #" + str(step['number']) + ": " + step['step'])

        # Some ingredients are missing: Print Missing Ingredients
        elif item['missedIngredientCount'] > 0:
            print("Need Ingredients to make " + item['title'])
            print("Missing Ingredients:")
            for ingred in item['missedIngredients']:
                print(str(ingred['amount']) + " " + ingred['unit'] + " " + ingred['name'])

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

