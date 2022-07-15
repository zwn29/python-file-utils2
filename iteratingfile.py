# iterating thorugh a file

with open('text.txt') as file:
    for line in file:
        print(line.upper())


# if we don't want the line gap then we need a string method called strip()

with open('text.txt') as file:
    for line in file:
        print(line.strip().upper())
        

file = open('text.txt')
lines = file.readlines()
file.close()
lines.sort()
print(lines)