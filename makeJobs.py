import os
import sys
import json

# Read in config file
with open('config.json') as data_file:
    data = json.load(data_file)

# Declare variables
job = data["data"]["job"]
log = data["data"]["log"]
directory = data["data"]["directory"]
filename = data["data"]["filename"]

if __name__ == '__main__':
    rootdir = sys.argv[1]
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file
            if filepath.endswith(".mkv"):
                program = "python3 checkFile.py "
                directoryfinal = directory + job + "/"
                directorylog = directory + log + "/"
                if not os.path.exists(os.path.expanduser(directoryfinal)):
                     os.mkdir(os.path.expanduser(directoryfinal))
                if not os.path.exists(os.path.expanduser(directorylog)):
                     os.mkdir(os.path.expanduser(directorylog))
                arguments = directoryfinal + ' "' + os.path.dirname(filepath)  + '/" "' + os.path.basename(filepath) + '" ' + directorylog
                commandcmd = program + arguments
                print(commandcmd)
                os.system(commandcmd)
