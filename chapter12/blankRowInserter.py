#! /usr/bin/python3
# blankRowInserter.py - Inserts blank rows into the spreadsheet.

import openpyxl, sys

N, M = int(sys.argv[1]), int(sys.argv[2])

read_wb = openpyxl.load_workbook(sys.argv[3])
read_sheet = read_wb.active
write_wb = openpyxl.Workbook()
write_sheet = write_wb.active

for i in range(1, N):
    for j in range(1, read_sheet.max_column):
        write_sheet.cell(row=i, column=j).value = read_sheet.cell(row=i, column=j).value

for i in range(N, read_sheet.max_row + 1):
    for j in range(1, read_sheet.max_column):
        write_sheet.cell(row=i+M, column=j).value = read_sheet.cell(row=i, column=j).value

write_wb.save('updated' + sys.argv[3])