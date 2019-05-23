def printTable(data):
    colWidths = []
    for i in range(len(data)):
        longest = len(data[i][0])
        for j in range(1, len(data[i])):
            if len(data[i][j]) > longest:
                longest = len(data[i][j])
        colWidths.append(longest)
    for k in range(len(data[0])):
        for l in range(len(data)):
            print(data[l][k].rjust(colWidths[l]), end=' ')
        print()
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)