
with open('test.txt', 'r') as f:
    
    for line in f:
        print(line, end='')

    f_contents = f.read(10)

    while len(f_contents)>0:
        print(f_contents, end='*')#more clear to see youre looping 10 chars at a time
        f_contents = f.read(10)

    print(f.tell())#saying what position in file you are in

    
    f_contents = f.read(100)
    # f_contents = f.readlines()
    # f_contents = f.readline()
    print(f_contents)#prints out all content in the file
    print(f_contents, end='')
    f.seek(0)#sets the position back to 0



#f = open('test.txt', 'r')#'w' write, 'a' append, 'r+' read and write

#print(f.name)
print(f.closed)
#f.close()


with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


with open('bronx.jpg', 'rb') as rf:
    with open('bronx_copy.jpg', 'wb') as wf:
        # for line in rf:
        #     wf.write(line)
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)



