# Read a local file - So this opens the file
file = open('text_file.txt', 'r')

# Read the Whole File - Try running this twice. it is interesting it only works once!
file.read()

#-----------------------------------------------------------------------------

# Read a local file - So this opens the file ( run this before running the other commands)
file = open('text_file.txt', 'r')

#-----------------------------------------------------------------------------

# Read file line by line - im not used to this format yet - taken online
count = 0

# this seems to read all the lines at the same time
file.readlines()


# literally reads one line at a time until it is empty
file.readline()

# the formal method to read one line at a time - the format is still unfamiliar - got this online
for line in file:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

# Read file line by line - it looks normal
for line in file:
    count += 1
    print(line.strip())

# Read file line by line - by taking out the .strip() method, there is no newline character
for line in file:
    print("Line: " + line)

# this should work also
while len(file.readline()) > 0:
    print(file.readline())


#-----------------------------------------------------------------------------
# practice writing to a file - this seems to overwrite the file

file = open('text_file.txt', 'r')
file.readlines()

# open the file - this seems to overwrite the file in question vs. appending it
file = open('text_file.txt', 'w')

# lets use a list to write to the file
list = ['joe','moe','sharon','1arry']

file.write(list[1] + "-")

file.write(list[3] + "-")

file.write(list[0] + "-")

file.close()

file = open('text_file.txt', 'r')
file.readlines()

#-----------------------------------------------------------------------------
# this mode apparently appends a file
file = open('text_file.txt', 'r')
file.readlines()

# open the file - this seems to overwrite the file in question vs. appending it
file = open('text_file.txt', 'a')

# lets use a list to write to the file
list = ['joe','moe','sharon','1arry']

file.write(list[1] + "-")

file.write(list[3] + "-")

file.write(list[0] + "-")

file = open('text_file.txt', 'r')
file.readlines()

# use a for loop for fun
count = 0

file = open('text_file.txt', 'w')

for item in list:
    file.write(list[count])
    count += 1
file.close()

file = open('text_file.txt', 'r')
file.readlines()

#-----------------------------------------------------------------------------
# Experiment with the .writelines() method
file = open('text_file.txt', 'r')
file.readlines()

# open the file - since it is a it will append to the file
file = open('text_file.txt', 'a')

# lets use a list to write to the file
list = ['joe','moe','sharon','1arry']

file.writelines(list)
file.close()

file = open('text_file.txt', 'r')
file.readlines()



