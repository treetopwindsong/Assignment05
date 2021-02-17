#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# RBell, 2021-Feb-13, Expanded on TODO
# RBell, 2021-Feb-15, added functionality of loading existing data
# Rbell, 2021-Feb-15, debugged save data text file to stop only saving keys
# RBell, 2021-Feb-16, added .pop() method and improved save functionality
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dicRow = {}  # dict of data row
strFileName = 'CDInventoryExperiment.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break

    if strChoice == 'l':
        # TODO Add the functionality of loading existing data => use dictionaries as inner data type/list of dictionaries
        #lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': int(lstRow[0]), 'CD title': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()

    elif strChoice == 'a':
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')#provided code used this format, so used assigning to variable first format
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'CD title': strTitle, 'artist': strArtist}
        lstTbl.append(dicRow)

    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')

    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        ID = int(input('Enter ID of CD to be deleted: '))-1 # alligns id # with index
        value =lstTbl.pop(ID)
        print('The entry deleted is: ', value)
        #del lstTbl[ID] => need to delete row

    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')#does write over write?
        for row in lstTbl:
            strRow = ''
            for items in row.values():
                strRow += str(items) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')




