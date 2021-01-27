# open file
# second argument 'w' for write, 'a' for append, 
# 'r' for read, 'r+' for read and write,
# 'b' opens the binary format
f = open('filecreatedbyPy', 'w')
f.close()

with open('filecreatedbyPy','r+') as f:
    f.write("This is a file created by Python IO system.\n")
    f.write("This the second line of this file.\n")
    for i in range(20):
        f.write('{} '.format(i))
    data_read = f.read() # read() method only return strings
    line_read = f.readline()
    
with open('filecreatedbyPy') as f:
    lines = f.readlines
    print(lines)
        
print("If the file was closed: ", f.closed)

