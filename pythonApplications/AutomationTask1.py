#First Automation Program(Script)
import schedule
import time
import datetime

def Fun():
    print("Inside fun")

def main():
    print("Inside task scheduler")

    schedule.every(1).minutes.do(Fun)   #function gets registered by scheduler

    while(True):                        #Unconditional infinite loop
        schedule.run_pending()          #terminal should be on at basic level but there are options
        time.sleep(1)

if __name__ == "__main__":
    main()