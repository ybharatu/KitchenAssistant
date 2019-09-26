from pymongo import MongoClient


# Function that removes an item from the database
def remove_item( food, cmd ):
    # Asks name of item to remove (TODO: Parse information from initial command and ask remaining info)
    item_name = input("Name: ")

    # Creates query to search
    myquery = { "name" : item_name }

    # Gets appropriate item
    r_item = food.find_one({ "name" : item_name})

    if r_item is not None:
        # Removes item
        food.delete_one( { "_id" : r_item.get("_id") })
    else:
        print("Item " + item_name + " is not in database")


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


# Main Driving Function
if __name__ == "__main__":
    # Enable Mongo Client
    client = MongoClient('localhost', 27017)

    # Create Database
    db = client['Ingredients']

    # Create Database list
    food = db.food

    while True:
        # Asks user for command and formats for parsing
        cmd = input("Command: ")
        cmd = cmd.strip().lower()

        # Parses command
        if cmd == "add":
            add_item(food, cmd)
        elif cmd == "print":
            print_items(food, cmd)
        elif cmd == "remove":
            remove_item(food, cmd)
        elif cmd == "quit" or cmd == "exit":
            break
        else:
            # TODO: Should have a -h or -verbose option
            print("Not a valid command")
