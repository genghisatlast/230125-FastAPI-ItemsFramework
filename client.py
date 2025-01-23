import requests
#import asyncio
BASE_URL = "http://127.0.0.1:7777"

# Create an item
def create_item(item_id, item_name, item_price):
    response = requests.post(f"{BASE_URL}/items/", json={
        "item_id": item_id,
        "item_name": item_name,
        "item_price": item_price
    })
    return response.json()

# Update an item
def update_item(item_id, item_name, item_price):
    response = requests.put(f"{BASE_URL}/items/{item_id}", json={
        "item_id": item_id,
        "item_name": item_name,
        "item_price": item_price
    })
    return response.json()

# Delete an item
def delete_item(item_id):
    response = requests.delete(f"{BASE_URL}/items/{item_id}")
    return response.json()

# Get an item
def get_item(item_id):
    response = requests.get(f"{BASE_URL}/items/{item_id}")
    return response.json()

#async def promptmac():
#    Finput = await input("type 'LS' to list all items OR type the name of the item(EXACTLY).")
#    return Finput


# EXAMPLE usage

if __name__ == "__main__":

    #asyncio.run(promptmac())
    while KeyboardInterrupt:

        Finput = input("What do you want to do? -getitem -delitem -upditem -crtitem \n")
        if Finput == "-getitem":
            itemid = int(input("Type the ID number of the item that you want to GET: "))
            print(get_item(itemid))
        elif Finput == "-delitem":
            itemid = int(input("Type the ID number of the item that you want to DELETE: "))
            print(delete_item(itemid))
        elif Finput == "-upditem":
            itemid = int(input("Type the ID number of the item that you want to UPDATE: "))
            itemname = input("Type the name of your item: ")
            itemprice = float(input("Type the price of your item: "))
            print(update_item(itemid,itemname,itemprice))
        elif Finput == "-crtitem":
            itemid = int(input("Type the ID number of the item that you want to CREATE: "))
            itemname = input("Type the name of your item: ")
            itemprice = float(input("Type the price of your item: "))
            print(create_item(itemid,itemname,itemprice))
        else: print("\nError: Unrecognized Input!\n")

    #print("\n\n Current item(s): \n\n")
    #print(create_item(1, "Laptop", 999.99))
    #print(get_item(1))
    #print(update_item(1, "Gaming Laptop", 1299.99))
    #print(delete_item(1))
