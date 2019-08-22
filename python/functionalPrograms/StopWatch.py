# Simulate Stopwatch Program
# Desc -> Write a Stopwatch Program for measuring the time that elapses between the start and end clicks
# I/P -> Start the Stopwatch and End the Stopwatch
# O/P -> Print the elapsed time.
import time
start=0
active=False
duration=0.0

class StopWatch:    
 
    
    def start():
        global start
        global active
        start=(time.time() * 1000)
        active=True

    def stop(): 
        global duration
        global active  
        duration=duration+((time.time() * 1000)-start )
        active=False

    def reset():
        global active
        global start
        active=False
        start=0

    def restart():
        stop() 
        start() 

    def  getElaspedTime():
        global active
        global start
        if(active):
         return duration+((time.time() * 1000)-start ) 
        else:
         return duration     


    start()
    stop()
    time=getElaspedTime()
    print(time)
