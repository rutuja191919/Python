#Terminate the program after some time - 2 approach
import schedule
import time
import datetime
import sys

i = 1
def Fun():
    global i
    if i == 2:
        sys.exit()
    print("Inside fun at time : ",datetime.datetime.now())
    print(i)
    i = i + 1

def main():
    print("Inside task scheduler")
    print("Current time is :",datetime.datetime.now())

    schedule.every(1).minutes.do(Fun)   #function gets registered by scheduler

    while(True):                        #Unconditional infinite loop
        schedule.run_pending()          #terminal should be on at basic level but there are options
        time.sleep(1)

if __name__ == "__main__":
    main()