import os
import sys

if __name__ == '__main__':
    rootdir = sys.argv[1]
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".mkv"):
                program = "python3 checkFile.py "
                arguments = '~/checkerrr/Job/1/ "' + os.path.dirname(filepath)  + '/" "' + os.path.basename(filepath) + '" ~/checkerrr/Log/'
                commandcmd = program + arguments
                print(commandcmd)
                os.system(commandcmd)
