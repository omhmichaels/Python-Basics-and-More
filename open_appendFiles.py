#
#
#

## Writing to a file

text = "Sample Text to save \n New Line"

# First specify file to open to write to
# open function passes two parameters. 
# File name, intention ie read, write , open, execute?
saveFile = open('exampleFile.txt', 'w')

# Write text variable to file variable 
saveFile.write(text)

# Always want to close files
saveFile.close()


## Read from file

# Opens then uses read function.
readMe = open('exampleFile.txt', 'r').read()

# Reads it into a list format, ie line by line
readMe2 = open('exampleFile.txt', 'r').readlines()

# Appending to file
# Same format as above

appendMe = '\n A new bit of information \n'

appendFile = open('exampleFile.txt', 'a')
appendFile.write(appendMe)
appendFile.close

