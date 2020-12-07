import csv
import sys
import os

Job = ""
Directory = ""
Filename = ""
Log = ""

if __name__ == '__main__':
    Job = sys.argv[1]
    Directory = sys.argv[2]
    Filename = sys.argv[3]
    Log = sys.argv[4]

    #print(Job)
    #print(Directory)
    #print(Log)
    #print(Filename)

    filetoCheck = Directory + Filename
    #print(filetoCheck)

    logtoFile = Log + Filename + ".log"
    #print(logtoFile)

    checkCMD = 'ffmpeg -v error -i "' + filetoCheck + '" -f null - 2>&1 | tee "' + logtoFile + '"'
    #print(checkCMD)
    os.system(checkCMD)
