with open('test.txt', 'r') as File1:
    file_stuff=File1.read()     #string
    print(file_stuff)
print(File1.closed)
print(file_stuff)