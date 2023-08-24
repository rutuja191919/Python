#Checksum is calculated by MD5 algorithm
#Add this in the program : now we are going to delete duplicate file and check log for that or backup it in the folder
#log file creation

import os
from sys import *
import hashlib
import time

def DeleteFiles(dict1):
    results = list(filter(lambda x: len(x) > 1,dict1.values()))

    iCnt = 0;

    if len(results) > 0:
        for result in results:
            for subresult in result:
                iCnt+=1
                if iCnt >= 2:
                    os.remove(subresult)
            iCnt = 0
    else:
        print("No duplicate files found")

def hashfile(path, blocksize = 1024):
    afile = open(path,'rb')  #open file in binary mode
    hasher = hashlib.md5()   #hasher is name of object

    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        #update : 1024 byte dilya,a kiti vela,b kiti vela he calculaton formulyala pathvta positions check karyasathi
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups ={}

    if exists:
        for foldername, subfolders, filenames in os.walk(path):
            for fnames in filenames:
                path = os.path.join(foldername, fnames)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)    #file_hash : key and path : value
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid path")

def PrintResults(dict1):
    results = list(filter(lambda x: len(x) > 1,dict1.values()))

    if len(results) > 0:
        print("Duplicates found")
        print("the following files are duplicate")
        for result in results:
            for subresult in result:
                print('\t\t%s'% subresult);
    else:
        print("No duplicate files found")


def main():
    print("Duplication File Checksum")

    if(len(argv) != 2):
        print("Insufficient arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("Help : This script will travel the directory and display the name of all entries")
        exit()

    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Application_name Directory_name")
        exit()

    try:
        arr = {}
        startTime = time.time()
        arr = FindDuplicate(argv[1])
        PrintResults(arr)
        DeleteFiles(arr)
        stopTime = time.time()

        print("The time required is : ",(stopTime - startTime))

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid Input",E)

if __name__ == "__main__":
    main()