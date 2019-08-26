def calculatePayment(year,rate,principal):
    n=12*year
    r=rate/12*100
    payment=principal*r/1-pow((1+r),(-n))
    print(payment)