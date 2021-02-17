#------------------------------------------#
# Title: CDInventory.py
# Desc: CD Inventory with dictionaries for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# RBell, 2021-Feb-13, Expanded on TODO
# RBell, 2021-Feb-15, added functionality of loading existing data
# Rbell, 2021-Feb-15, debugged save data text file to stop only saving keys
# RBell, 2021-Feb-16, added .pop() method and improved save functionality
#------------------------------------------#

strChoice = ''
lstTbl = []
dicRow = {}
strFileName = 'CDInventory.txt'
objFile = None


print('The Magic CD Inventory\n')
while True:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()
    print()

    if strChoice == 'x':
        break

    if strChoice == 'l':
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': int(lstRow[0]), 'CD title': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()

    elif strChoice == 'a':
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'CD title': strTitle, 'artist': strArtist}
        lstTbl.append(dicRow)

    elif strChoice == 'i':
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')

    elif strChoice == 'd':
        ID = int(input('Enter ID of CD to be deleted: '))-1
        value =lstTbl.pop(ID)
        print('The entry deleted is: ', value)

    elif strChoice == 's':
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for items in row.values():
                strRow += str(items) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')




