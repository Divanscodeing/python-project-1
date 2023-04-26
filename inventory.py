#!/usr/bin/env python
# coding: utf-8

# In[9]:


'''
Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods
like add_item, update_item, and check_item_details. 
Use a dictionary to store the item details, where the key is the item_id and the value is a dictionary 
containing the item_name, stock_count, and price.
'''
class Inventory:
    
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_id, item_name, stock_count, price):
        self.inventory[item_id] = {"item_name": item_name, "stock_count": stock_count, "price": price}
        
    def update_item(self, item_id, stock_count, price):
        if item_id in self.inventory:
            self.inventory[item_id]["stock_count"] = stock_count
            self.inventory[item_id]["price"] = price
        else:
            print("Item not found in inventory.")

    def check_item_details(self, item_id):
        if item_id in self.inventory:
            item = self.inventory[item_id]
            return f"Product Name: {item['item_name']}, Stock Count: {item['stock_count']}, Price: {item['price']}"
        else:
            return "Item not found in inventory."

I = Inventory()

I.add_item(1,"laptop",100,500.00)
I.add_item(2,"mobile",105,400.00)
I.add_item(3,"desktop",10,200.00)
I.add_item(4,"ipad",19,100.00)
I.add_item(5,"ipod",140,1100.00)
I.add_item(6,"iwatch",110,300.00)

print("Item details")
print("**********************************************************************************************************************")

print(I.check_item_details(1))
print(I.check_item_details(2))
print(I.check_item_details(3))
print(I.check_item_details(4))
print(I.check_item_details(5))
print(I.check_item_details(6))
print("updating iwatch")
print("**********************************************************************************************************************")
I.update_item(6, 50, 200.00)
print("**********************************************************************************************************************")
print(I.check_item_details(6))


# In[4]:


I.add_item(1,"laptop",100,500.00)
inventory = {}
item_id = 2
item_name = "iphone 14"
stock_count = 5
price = 799
inventory[item_id] = {"item_name": item_name, "stock_count": stock_count, "price": price}
print(inventory)


# In[ ]:




