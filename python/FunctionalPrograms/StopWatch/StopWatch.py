# Simulate Stopwatch Program
# Desc -> Write a Stopwatch Program for measuring the time that elapses between the start and end clicks
# I/P -> Start the Stopwatch and End the Stopwatch
# O/P -> Print the elapsed time.


import StopWatchBL as sb

print("1.press '1' to start the stopwatch",'\n',"2. press '2' to stop the watch",'\n',"3.press '3' to restart",'\n',
"4.press '4' to reset",'\n',"5.press '5' to get the elapsed time",'\n',"press '0' for exiting the application")

i=int(input())
flag=True
while(flag):
    if(i==1):
        sb.start()
        i=int(input())
    if(i==2):
        sb.stop()
        i=int(input())
    if(i==3):
        sb.restart()
        i=int(input())
    if(i==4):
        sb.reset() 
        i=int(input())
    if(i==5):
        print("the elapsed time between start and end clicks is =",sb.elapsedtime())
        i=int(input())
    if(i not in (1,0,2,3,4)):
        print("press valid key")
        break
    if(i==0):
        print('no operation wanted')
        break
        
    