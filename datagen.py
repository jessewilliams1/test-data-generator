import csv

run = True

# Opens output.csv for editing. If it does not exist, creates it.
csvWriter = csv.writer(open('output.csv', 'wb'))

while run:
    columnCountInput = raw_input('\nNumber of columns:\n')
    columnCount = int(columnCountInput)
    columnNameList = []
    listPosition = 1

    #Iterates through the number of columns to get the names for each
    while columnCount > 0:
        columnNameInput = raw_input('\nName for column ' + str(listPosition) + ':\n')
        columnCount -= 1
        listPosition += 1
        columnNameList.append(columnNameInput)

    rowCountInput = raw_input('\nNumber of rows to be generated: \n')
    rowCount = int(rowCountInput)

    rowNumber = 1 # Incremented value that is stringed and added to the end of each column

    singleRowList = []

    while rowCount > 0:
        for x in columnNameList:
            outputRow = x + str(rowNumber)
            #print outputRow, # Comment this line out to ommit visual display
            singleRowList.append(outputRow)

        csvWriter.writerow(singleRowList)
        singleRowList = [] # Sets the list top blank, for the next row to be written
        #print # Blank line, to seperate between iterations (commend out to ommit)
        rowNumber += 1
        rowCount -= 1
        
    # User prompt to quit or do another
    runInput = raw_input('\nGeneration complete! Do another? (y or n)\n')

    if runInput == 'y':
        run = True
    elif runInput == 'n':
        run = False
        
