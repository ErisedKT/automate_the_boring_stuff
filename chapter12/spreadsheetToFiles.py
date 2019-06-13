#! /usr/bin/python3
# spreadsheetToFiles.py - Writes columns of a spreadsheet into different text files.
# Usage: ./spreadsheetToFiles.py <workbook>

import openpyxl, sys

# Open spreadsheet.
wb = openpyxl.load_workbook(sys.argv[1])
sheet = wb.active

# Iterate over columns in sheet.
for column in sheet.columns:
    # Create filename for column.
    filename = 'Column' + str(column[0].column) + '.txt'
    
    with open(filename, 'w') as colFile:
        # Write contents of each cell to the file.
        for cell in column:
            if cell.value != None:
                colFile.write(cell.value + '\n')