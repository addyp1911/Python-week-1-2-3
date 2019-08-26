import time
start=0
active=False
duration=0.0


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
