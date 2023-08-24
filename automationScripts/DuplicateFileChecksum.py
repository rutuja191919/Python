#Checksum is calculated by MD5 algorithm

import os
from sys import *
import hashlib

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

def Display_Checksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolders, filenames in os.walk(path):
            for fnames in filenames:
                path = os.path.join(foldername, fnames)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')
    else:
        print("Invalid path")

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

    arr = Display_Checksum(argv[1])

if __name__ == "__main__":
    main()