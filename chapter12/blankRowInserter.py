#! /usr/bin/python3
# blankRowInserter.py - Inserts blank rows into the spreadsheet.
# Usage: ./blankRowInserter.py <start_row> <number_of_blank_rows> <workbook_name>

import openpyxl, sys

# N: Starting row.
# M: Number of blank rows.
N, M = int(sys.argv[1]), int(sys.argv[2])

# Open workbook.
wb = openpyxl.load_workbook(sys.argv[3])
sheet = wb.active

# Slice rows to be moved.
moveRows = tuple(sheet[str(N + M) + ':' + str(sheet.max_row)])[::-1]

# Change row attribute of Cell objects in moveRows.
for rowOfCellObj in moveRows:
    for cellObj in rowOfCellObj:
        cellObj.row += M

# Save updated file.
wb.save('updated_' + sys.argv[3])