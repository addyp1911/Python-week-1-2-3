# a.Desc :Create a JSON file having Inventory Details for Rice, Pulses and Wheats
# with properties name, weight, price per kg.
# b. Use Library : Java JSON Library , For IOS JSON Library use
# NSJSONSerialization for parsing the JSON .
# c. I/P ­> read in JSON File
# d. Logic ­> Get JSON Object in Java or NSDictionary in iOS. Create Inventory
# Object from JSON. Calculate the value for every Inventory.
# e. O/P ­> Create the JSON from Inventory Object and output the JSON String

import InventoryPulsesBL as ip
i=ip.Inventory()
i.calculate_total_price()
i.print_record()


