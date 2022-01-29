##########################################################################
##  
##  Prasad R. Bhosale  (328M_Prasad)
##  Wednesday (24/01/2022)
##
##  Directory Watcher : Script for the directory checking.
##########################################################################
import hashlib
import os
from sys import *

def DirectoryWatcher(path):
    
    flag = os.path.isabs(path)
    # checksum = []
    # md5_hash = hashlib.md5()
    if flag == False:
        path = os.path.abspath(path)
        
    exists = os.path.isdir(path)
    
    if exists : 
        
        for foldername,subfolder,filename in os.walk(path):
            print("Current folder is : "+foldername)
            
            for subf in subfolder:
                print("Sub folder of "+ foldername + " is : "+subf)
        
            for filen in filename:
                # hash_file = open(filen,"rb")
                # content = hash_file.read()
                # md5_hash.update(content)
                # digest = md5_hash.hexdigest()
                # print(digest)
                print("File inside "+foldername+" is : "+filen)
            print(" ")
        
    else:
        print("Invalid Path ..!!")

def main():
    print("----Directory Watcher by Prasad Bhosale ----")
    print("Application name : "+argv[0])
    
    if (len(argv)!=2):
        print("Error : Invalid number of arguments..")
        exit()
    if (argv[1]=="-h" or argv[1]=="-H"):
        print("This script is used to traverse specific directory. ")
        exit()
    if (argv[1]=="-u" or argv[1]=="-U"):
        print("Usage : Application Name AbsolutePath_of_Directory")
        exit()
    
    try:
        DirectoryWatcher(argv[1])
    
    except ValueError:
        print("Error : Invalid datatype of input ")
    except Exception : 
        print("Error : Invalid input ")
    
    
if __name__=="__main__":
    main()