def recursive(n):
    if n==1:
        return 1
    else:
        return n * recursive(n-1)
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
num=int(input("Enter the Number: "))
print("Factorial =",recursive(num))
print("Fibonacci=",fibonacci(num))

