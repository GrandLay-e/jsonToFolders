from pprint import pprint
from functions import *
import os
import sys

# Determine JSON file path and destination directory
if len(sys.argv) > 1 and sys.argv[1].endswith(".json"):
    jsonPath = sys.argv[1]
else:
    jsonPath = "exemple.json"

# Default destination is the script's directory
if len(sys.argv) > 2:
    destination = Path(sys.argv[2])
else:
    destination = Path(os.getcwd())

dirs = GetJson(jsonPath)
#Some error handling
if isinstance(dirs, Exception):
    print(f"Error reading JSON file: {dirs}")
    sys.exit(1)
if not isinstance(dirs, dict):
    print("The JSON file must contain a dictionary at the top level.")
    sys.exit(1)
if len(dirs) == 0:
    print("The JSON file is empty.")
    sys.exit(1)

listOfDirs, listOfFiles = loopDirs(dirs)
if not destination.exists():
    os.makedirs(destination, exist_ok=True)
os.chdir(destination)

[dir.create() for dir in listOfDirs if len(listOfDirs) > 0]
[file.create() for file in listOfFiles if len(listOfFiles) > 0]