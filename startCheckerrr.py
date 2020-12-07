import os
import sys
import json

# Read in config file
with open('config.json') as data_file:
    data = json.load(data_file)

log = data["libary"]

for each in log.values():
    program = "python3 makeJobs.py "
    checkerrrCmd = program + each
    os.system(checkerrrCmd)

