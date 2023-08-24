
import schedule
import time
import datetime

def Task_Minute():
    print("Task based on minutes gets scheduled at : ",datetime.datetime.now())

def Task_Hours():
    print("Task based on hours gets scheduled at : ",datetime.datetime.now())

def Task_Day():
    print("Task based on day gets scheduled at : ",datetime.datetime.now())

def main():
    print("Inside task scheduler")
    print("Current time is :",datetime.datetime.now())

    schedule.every(1).minutes.do(Task_Minute)   #Callback function by task scheduler
    schedule.every(1).hour.do(Task_Hours)
    schedule.every().saturday.at("18:35").do(Task_Day)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()