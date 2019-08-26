# Write a Util Static Function to calculate monthlyPayment that reads in three command-line 
# arguments P, Y, and R and calculates the monthly payments you would have to make over Y years 
# to pay off a P principal loan amount at R per cent interest compounded monthly. 
import MonthlyPaymentBL as mp
year=int(input("enter the years over which payment needs to be made= "))
rate=int(input("enter the rate of interest= "))
principal=int(input("enter the principal= "))
mp.calculatePayment(year,rate,principal)
