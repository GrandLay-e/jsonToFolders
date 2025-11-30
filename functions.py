import json
from pathlib import Path
import os
from classes import File, Folder

def GetJson(jsonFile):
    try: 
        with open(jsonFile, 'r') as f:
            return json.load(f)
    except Exception as e:
        return e
    
def loopDirs(d, sep = 0, currentPath : Path = Path(""), listOfFolders = None, listOfFiles = None):
    """Function that loops all directories given by the JSON file

    Args:
        d (dict): the content of the json file
        sep (int, optional): it helps for displaying files and folder with indents. Defaults to 0.
        currentPath (Path, optional): the current path (to not lose information with recursion). Defaults to Path("").
        listOfFolders (list, optional): Contains all folders the users wants to create. Defaults to [].
        listOfFiles (list, optional): Contains all files the users wants to create. Defaults to [].

    Returns:
        tuple: The list of folders and the list of files
    """
    if listOfFolders is None:
        listOfFolders = []
    if listOfFiles is None:
        listOfFiles = []
    # Loop through the dictionary
    for key, value in d.items(): 
        # If the value is a string, it could be a Folder or File
        if isinstance(value, str): 
            # Check if it's a Folder or File
            if value == "Folder": 
                # Add Folder object (name, parentPath)
                listOfFolders.append(Folder(d['Name'], currentPath) ) 
                currentPath = currentPath.joinpath(d['Name']) 
            # Check if it's a File
            elif value == "File": 
                # Add File object (name, parentPath)
                listOfFiles.append(File(d['Name'], currentPath) )
            print(f" {'\t' * sep}{key} -> {value}") 
        
        # Recursive calls for nested content
        if key == "content" and isinstance(value, list): 
            for item in value: 
                if isinstance(item, dict): 
                    loopDirs(item, sep + 1, currentPath, listOfFolders, listOfFiles) 
        elif isinstance(value, dict): 
            loopDirs(value, sep + 1, currentPath, listOfFolders, listOfFiles) 
    
    return listOfFolders, listOfFiles # Return the lists of Folders and Files
