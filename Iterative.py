def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac


num=int(input("Enter the number:"))
print(factorial(num))