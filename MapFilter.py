#--------------------------------MAP-------------------------------------------
# number=["1","3","4"]
# for i in range(len(number)):     #normal way to convert str in integer
#     number[i]=int(number[i])
# number=list(map(int,number))
# a=number[1]+number[2]
# print(a)
# print(number)
#
# number1=[1, 3, 4]
# number1=list(map(str,number1))
# print(number1)
#
# def sq(a):
#     return a*a
#
# num=[1,2,3,4,5,6]
#
# square=list(map(sq,num))
# abc=list(map(lambda z: z*z ,num))
# print(square)
# print(abc)

# def Square1(a):
#     return a*a
#
# def Cube1(a):
#     return a*a*a
#
# Func=[Square1,Cube1]
# for i in range(5):
#     val=list(map(lambda x:x(i),Func))
#     print(val)
#--------------------------------Filter-------------------------------------------
#
# list1=[1,2,3,4,5,6,7,]
# def is_greater_5(num):
#     return num>5
#
# gr_than_5=list(filter(is_greater_5,list1))
# print(gr_than_5)
#--------------------------------REDUCE-------------------------------------------
from functools import reduce
list2=[1,2,3,4,5]
num=reduce(lambda x,y:x+y,list2)
print(num)