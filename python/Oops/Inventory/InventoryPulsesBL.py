# ----------------------------------InventoryDetails prg-----------------------------------------------
# InventoryDetails.py
# date : 27/08/2019
# method to print the inventory records


def calculate_total_price(inventory_dict):
    for key,value in inventory_dict.items():
        calc_tot=1
        for j in value:
#retrieving the quantity of a particular category of foodstock            
            if(j=='quantity'):     
                quantity=value.get(j)
                calc_tot*=int(quantity)
#retrieving the price per kg of the category                
            if(j=='price per kg'):
                price=value.get(j)
#the total price of the inventory stock is printed                
                print("the total price of the inventory stock of this category is= ",calc_tot*int(price))   


def print_inventory_record(inventory_dict):
#the entire inventory record list is printed    
    for key,value in inventory_dict.items():
        print()
        for k,v in value.items():
            print(k,v,end=" ") 
    print()           


