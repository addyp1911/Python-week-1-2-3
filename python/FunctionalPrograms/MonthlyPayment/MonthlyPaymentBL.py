
# ----------------------------------MonthlyPayment prg-----------------------------------------------
# MonthlyPayment.py
# date : 26/08/2019
# method to print calculates the monthly payments you would have to make over Y years 
# to pay off a P principal loan amount at R per cent interest compounded monthly. 



def calculatepayment(year,rate,principal):
    n=12*year
    r=rate/12*100
    payment=principal*r/1-pow((1+r),(-n))
    print("the monthlypayments to pay off the loan is ",payment)