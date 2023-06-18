# f=open("Nikhil.txt","a")
# a=f.write("NIkhil & Swapnil are best friends\n")
# print(a)
# f.close()

#Handle , read and write
f=open("Nikhil.txt","r+")
print(f.read())
f.write("Thank You!") 
f.close()