# ----------------------------------InventoryDetails prg-----------------------------------------------
# InventoryDetails.py
# date : 27/08/2019
# method to print the inventory records

import json
class Inventory:

    try:
        def __init__(self):
            with open("pulses_inventory.json", "r") as my_file:
                self.inventory = json.load(my_file)
                print(self.inventory)    
                                       # load() converts file into python object from json
                                       #inventory is a dictionary

        def print_record(self):
            for records in range(len(self.inventory["inventory"])):
                print(self.inventory["inventory"][records])
     
        def calculate_total_price(self):
            total_price=0
            for records in range(len(self.inventory["inventory"])):
                for key,value in self.inventory["inventory"][records].items():
                    if(key =="quantity"):
                        total_price=int(self.inventory["inventory"][records][key])
                    if(key=="price per kg"):
                        total_price*=int((self.inventory["inventory"][records][key]))
                print("the total price of "+self.inventory["inventory"][records]["name"]+" is",total_price)
            
    except(FileNotFoundError):
        print("the file cannot be found")        


