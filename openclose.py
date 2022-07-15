file = open('text.txt')

print(file.readline())

# print(file.readline())
# the read() method ll start reading from the end of readline() to the end of the file 
# the readline() method ll only read one line

print(file.read())
# finally we close the file with file.close() method

file.close()

# we need to close the file coz when we open 
# the file it cannot be accessed by other programs 
# that's why we need to close it after use

