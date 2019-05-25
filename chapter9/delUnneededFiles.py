#! /usr/bin/python3
# delUnneededFiles.py - Prints files in a folder tree with file
# size greater than a certain amount (in MBs).

import os

def deleteFiles(folder, size):

    # Make sure folder is an absolute path.

    folder = os.path.abspath(folder)

    # Walk through folder tree.

    for foldername, subfolders, filenames in os.walk(folder):
        # print('Looking inside %s...' % foldername)
        
        # Check if any files have a file size greater than size.

        for filename in filenames:
            if os.path.getsize(os.path.join(foldername, filename)) > size * 1000000:
                print(os.path.join(foldername, filename))   # prints large files
                print()


deleteFiles('/home/sanya/Desktop/Everything\'s_in_here', 1)