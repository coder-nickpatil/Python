# f=open("Nikhil.txt")
# print(f.tell())   #tell()-> Give File Pointer..
# print(f.readline())
# print(f.tell())
# f.seek(10)     #seek()-> reset our file pointer
# print(f.readline())
# print(f.tell())
arr=[]
for i in range(0,a):
    arr.append(int(input()))

b=int(input())
c=int(input())

arr2=[]


for i in range(0,len(arr)):
    if (arr[i] >b and arr[i] <c):
        arr2.append(arr[i])

print(*arr2)
