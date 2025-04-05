"""
# write mode
#f = open("pk2.txt", "w") # this is write mode
f=open("pk2.txt", "a") # this is append mode they add a text at the end of print text
a=f.write("what the hell \t \n ")
print(a)
f.close()
"""

# read and write both modes

f=open("pk2.txt", "r+") # this is read and write function using + operator 
print(f.read())
f.write("Thank You")
f.close()
