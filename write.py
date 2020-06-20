Lines=['This is line A\n','This is line B\n','This is line C\n']
with open('test2.txt','w') as File1:       #the file will be created if not exist
    for line in Lines:
        File1.write(line)

with open('test2.txt','w') as File1:        # it will overlap the content of text2.txt
    File1.write("this is line d")

with open('test.txt','r') as readfile:
    with open('test2.txt','w') as writefile:
        for line in readfile:
            writefile.write(line)