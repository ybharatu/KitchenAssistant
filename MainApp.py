from pymongo import MongoClient


# Function that prints out all items
def print_items( food, cmd ):
    for item in food.find():
        print(item)


# Function that adds item to database
def add_item( food, cmd ) :
    item_name = input("Name: ")
    quantity = input("Quantity: ")
    expiration_date = input("Expiration Date (Press Enter if N/A): ")

    item_entry = {
        'name': item_name,
        'quantity': quantity,
        'expire': expiration_date
    }
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
        # Asks user for command
        cmd = input("Command: ")

        if cmd.strip().lower() == "add":
            add_item(food, cmd)
        if cmd.strip().lower() == "print":
            print_items(food, cmd)

