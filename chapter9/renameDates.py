#! /usr/bin/python3
# renameDates.py - Renames filenames with American 
# MM-DD-YYYY date format to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the
# American date format

datePattern = re.compile(r'''^(.*?)
    ((0|1)?\d)-
    ([0-3]?\d)-
    ((19|20)\d\d)
    (.*?)$
    ''', re.VERBOSE)

# Loop over the files in the working directory

for amerFilename in os.listdir('.'): 
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    
    if mo == None:
        continue

    # Get the different parts of the filename.

    beforePart = mo.group(1)  
    dayPart = mo.group(4)
    monthPart = mo.group(2)
    yearPart = mo.group(5)
    afterPart = mo.group(7)

    # Form the European-style filename

    euroFilename = beforePart + dayPart + '-' \
        + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    
    absWorkingDir = os.path.abspath('.')
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    amerFilename = os.path.join(absWorkingDir, amerFilename)

    # Rename the files.

    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)
