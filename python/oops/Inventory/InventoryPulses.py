# a.Desc :Create a JSON file having Inventory Details for Rice, Pulses and Wheats
# with properties name, weight, price per kg.
# b. Use Library : Java JSON Library , For IOS JSON Library use
# NSJSONSerialization for parsing the JSON .
# c. I/P ­> read in JSON File
# d. Logic ­> Get JSON Object in Java or NSDictionary in iOS. Create Inventory
# Object from JSON. Calculate the value for every Inventory.
# e. O/P ­> Create the JSON from Inventory Object and output the JSON String

import json
import InventoryPulsesBL as ip
with open("/home/admin1/Desktop/pulses_inventory.json",'r') as file:
#the entire json file is loaded and saved into the inventory dictionary which has a nested dictionary of item details    
    inventory_dict=json.load(file)
    print(inventory_dict)
    ip.calculate_total_price(inventory_dict)
    ip.print_inventory_record(inventory_dict)
