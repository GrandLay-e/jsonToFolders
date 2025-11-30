from pprint import pprint
from functions import *
import os
import sys

if len(sys.argv) > 1 and sys.argv[1].endswith(".json"):
    jsonPath = sys.argv[1]
else:
    jsonPath = "exemple.json"

destination = Path(os.path.join(__file__)).parent
print(destination)

dirs = GetJson(jsonPath)
listOfDirs, listOfFiles = loopDirs(dirs)
pprint(listOfDirs)
pprint(listOfFiles)

# [dir.create() for dir in listOfDirs]
# [file.create() for file in listOfFiles]