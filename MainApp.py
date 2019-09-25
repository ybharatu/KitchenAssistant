from pymongo import MongoClient


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
        if cmd == "print":
            print_items(food, cmd)
        if cmd == "quit" or cmd == "exit":
            break
