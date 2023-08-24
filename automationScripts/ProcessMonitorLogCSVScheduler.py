#Use pandas for CSV file generation in python : Extension: csv/xls
#Use tensorflow

import os
import psutil
import schedule
import time
import pandas as pd
from sys import *

def Display():
    print("hello")

def ProcessDisplay(log_dir = "Marvellous"):
    print("Inside process")
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    seperator = "-" * 80
    t =((time.ctime()).replace(" ",""))
    new_t = t.replace(":","-")
    #print(t)
    log_path = os.path.join(log_dir,"MarvellousLog%s.csv" % new_t)  #instead of time.ctime() use datetime.datetime()
    f = open(log_path,'w')
    f.write(seperator + "\n")
    f.write("Marvellous Infosystems Process Logger : " + time.ctime()+"\n")
    f.write(seperator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms/(1024 *1024)
            listprocess.append(pinfo)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    df = pd.DataFrame(listprocess)
    df.to_csv(log_path,index = False,sep = '|')
    #for element in listprocess:
        #f.write("%s\n"%element)

def main():
    print("-------Marvellous Infosystems by Piyush Khairnar---------")
    print("Application name : "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()
    if(argv[1] ==  "-h") or (argv[1] == "-H"):
        print("This script is used log record of running processes")

    if(argv[1] == "-u")or (argv[1] == "-U"):
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        schedule.every(1).minutes.do(lambda: ProcessDisplay(argv[1]))

        while (True):  # Unconditional infinite loop
            schedule.run_pending()  # terminal should be on at basic level but there are options
            time.sleep(1)

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as e:
        print("Error : Invalid input",e)

if __name__ == "__main__":
    main()