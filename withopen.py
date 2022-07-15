# we don't need to close the file explicitly in the with open() method
# it's a better alternative to the open() and close() methods

with open('text.txt') as file:
    print(file.readline())

