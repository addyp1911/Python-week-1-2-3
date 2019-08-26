def sqrt(c):
    t=c
    epsilon=1e-15
    while(abs(t- (c/t))>epsilon*t):
        t=(c/t + t)/2.0
    print(t)
