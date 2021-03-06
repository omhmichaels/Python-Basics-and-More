#
#
#
#


## errorHandling

#
#
#


# reading from CSV

import csv

# Create file
exampleCSV = open('exampleCSV.csv', 'w')
exampleCSV.write('1/1/17,Michael,01')

exampleCSV.close()

# comma seperated value
# comma is considered a delimiter

# converts file to csv
with open('exampleCSV.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)

    # prints out each row in csv
    for row in readCSV:
        print(row)
        print(row[0], row[1])


# Using cvs 
    dates = []
    names = []
    for row in readCSV:
        date = row[0]
        name = row[1]

        dates.append(date)
        names.append(name)

    whatName = input("what name")
    namex = name.index(whatName)

    theBirthday = dates[namex]

    print("Thier birthday is", namex)


### ERROR HANDLING
"""
# 
# Author: l33tH@x0rxxGh0u1
# 
# 
#
#
"""
# try and except
# Also used for porting between python 2 and 3

try:
    whatName = input("what name")
    if whatName in names:
        namex = name.index(whatName)
        theBirthday = dates[namex]
        print("Thier birthday is", namex)
    else:
        print("Name not found")
except Exception as e:
    print('the name is not in the list continuing')

# can have multiple exceptions i.e NameError, etc