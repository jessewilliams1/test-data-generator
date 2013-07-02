import csv

run = True

# Opens output.csv for editing. If it does not exist, creates it.
csvWriter = csv.writer(open('output.csv', 'wb'))

while run:
    fieldCountInput = raw_input('\nNumber of columns:\n')
    fieldCount = int(fieldCountInput)
    fieldNameList = []
    fieldPosition = 1

    #Iterates through the number of columns to get the names for each
    while fieldCount > 0:
        fieldNameInput = raw_input('\nName for column ' + str(fieldPosition) + ':\n')
        fieldCount -= 1
        fieldPosition += 1
        fieldNameList.append(fieldNameInput)


    lineCountInput = raw_input('\nNumber of rows to be generated: \n')
    lineCount = int(lineCountInput)

    rowCount = 1 # Incremented value that is stringed and added to the end of each column

    singleLineList = []

    while lineCount > 0:
        for x in fieldNameList:
            outputLine = x + str(rowCount)
            #print outputLine, # Comment this line out to ommit visual display
            singleLineList.append(outputLine)

        csvWriter.writerow(singleLineList)
        singleLineList = [] # Sets the list top blank, for the next row to be written
        #print # Blank line, to seperate between iterations (commend out to ommit)
        rowCount += 1
        lineCount -= 1
        
    # User prompt to quit or do another
    runInput = raw_input('\nGeneration complete, do another? (y or n)\n')

    if runInput == 'y':
        run = True
    elif runInput == 'n':
        run = False
        
