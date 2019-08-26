# ----------------------------------couponnumber prg-----------------------------------------------
# CouponNumbers.py
# date : 22/08/2019
# method to replace the name
import random

def calculateDistinctCoupons(coupon):
    isCollected=[None]*(coupon)
    distinct = 0
    value = 0
    count = 0
    i = 0
    while(i<coupon):
        value= int(random.uniform(0,1)*coupon)
        print(value)
        if(isCollected[value]==None):
            distinct += 1
            isCollected[value]=True
        i += 1    
    
    print("the no of random numbers needed",distinct)
 