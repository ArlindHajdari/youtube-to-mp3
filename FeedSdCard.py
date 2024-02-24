import sys
import os
import re
from pathlib import Path

dirlist = []

def SortFiles(rootdir):
    paths = sorted(Path(rootdir).glob('*.mp3'), key=os.path.getctime, reverse=True)
    numberOfZeros = len(str(len(paths)))
    identifier = 1

    for path in paths:
        basename = os.path.basename(path)
        enhancedBasename = basename.split('_', 1)[1] if  '_' in basename else basename
        
        modifiedBaseName = f'{str(identifier).zfill(numberOfZeros)}_{enhancedBasename}'
        
        newPath = str(path).replace(basename, modifiedBaseName)
        os.rename(path, newPath)

        identifier += 1

def OrganizeFiles(rootdir, dirlist):
    subfolders = [ os.path.join(rootdir, item).replace("\\",'/') for item in os.listdir(rootdir) if os.path.isdir(os.path.join(rootdir, item)) ]
    
    if subfolders:
        dirlist.extend(subfolders)
        
        SortFiles(rootdir)

        for folder in subfolders:
            OrganizeFiles(folder, dirlist)

    elif rootdir in dirlist:
        dirlist.remove(rootdir)
        SortFiles(rootdir)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Path to root folder not provided\nPlease use this template: py -3.8 script_name.py path_to_root_folder recursive_sort<-r, optional>")

    rootdir = sys.argv[1]
    recursiveFlag =  sys.argv[2] if len(sys.argv) == 3 else '0' 

    if recursiveFlag == '-r':
        OrganizeFiles(rootdir, dirlist)
    else:
        SortFiles(rootdir)