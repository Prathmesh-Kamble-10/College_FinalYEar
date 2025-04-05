#seek and tell funmction in readline funciton 
f = open("open.txt")
#print(f.tell()) # tell () function show where is pointer line its shows where is line

print(f.readline())
#print(f.tell())
f.seek(10)
print(f.readline())
f.seek(20) # seek() function used for return the line which you want
#print(f.tell())
print(f.readline())
f.close()