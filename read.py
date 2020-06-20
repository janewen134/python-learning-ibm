# with open('test.txt', 'r') as File1:
#     file_stuff=File1.read()     #string
#     print(file_stuff)
# print(File1.closed)     #Bool
# print(file_stuff)

# Python readline() method will return a line from the file when called.
# readlines() method will return all the lines in a file in the format of
# a list where each element is a line in the file.

# with open('test.txt','r') as File1:
#     file_stuff=File1.readline()
#     print(file_stuff)

# with open('test.txt','r') as File1:
#     for line in File1:
#         print(line)

fh = open('test.txt')
for line in fh.readlines():
  print(line)


with open('test.txt', 'r') as File1:
    f=File1.readlines(16)
    print(f)
    f=File1.readlines(5)
    print(f)
    f=File1.readlines(15)
    print(f)

# To rm '\n', you can:
with open("test.txt", "r") as f:
    data = f.readlines()
    print(data)
    a = data[0][:-1]
    b = data[1]
    print(a, b)

# or you can do the following:
with open("test.txt", "r") as f:
    data = f.read().splitlines()
    print(data)


