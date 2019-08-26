
# ----------------------------------StopWatch prg-----------------------------------------------
#StopWatch.py
# date : 26/08/2019
# method to print the time that elapses between the start and end clicks


import time
start=0
active=False
duration=0.0

def start():
    active=True
    start_time=time.time()
    return start_time

def stop():
    newDe = duration
    active=False
    start_time=start()
    newDe=newDe+(time.time()-start_time)
    return newDe

def restart():
    print("the time between start time and stop time",stop())
    start()

def reset():
    strt=0
    duration=0

def elapsedtime():          #method for measuring the time between start and end clicks of the stopwatch
     duration=stop()
     return duration    


    
