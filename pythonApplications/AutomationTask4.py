#Terminate the program after some time - 1 approach
import schedule
import time
import datetime
import sys

def ScriptTerminator():
    sys.exit()

def Fun():
    print("Inside fun at time : ",datetime.datetime.now())

def main():
    print("Inside task scheduler")
    print("Current time is :",datetime.datetime.now())

    schedule.every(1).minutes.do(Fun)   #function gets registered by scheduler
    schedule.every(1).minutes.do(ScriptTerminator)

    while(True):                        #Unconditional infinite loop
        schedule.run_pending()          #terminal should be on at basic level but there are options
        time.sleep(1)

if __name__ == "__main__":
    main()