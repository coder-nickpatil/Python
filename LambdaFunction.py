#Called as Anonymous functions..
# def Add(a,b):
#     return a+b      #Normal Function

# Add =lambda x,y: x+y  #Lambda Function
# print(Add(2,3))

def a_first(a):
    return a[0]
lst=[[2,1],[4,10],[1,3]]

# lst.sort(key=a_first)   #Sort list in list index vise
lst.sort(key=lambda x:x[1]) #Sort list in list index vise
print(lst)