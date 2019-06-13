#! /usr/bin/python3
# textToSpreadsheet.py - Turns several text files into a spreadsheet, with one line of text
# per row. First file will be in column A, second in B and so on.

import openpyxl, sys

files = sys.argv[1:]    # Store all file names in a list

# Read contents of files in a list.
contents = []
for f in files:
    with open(f) as txtFile:
        contents.append(txtFile.readlines())

# Create a workbook.
wb = openpyxl.Workbook()
sheet = wb.active
col = 1

# Assign content of files to worksheet.
for c in contents:
    row = 1
    for line in c:
        sheet.cell(row=row, column=col).value = line.strip('\n')
        row += 1
    col += 1

# Save workbook.
wb.save('textToSheet.xlsx')