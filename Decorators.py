# def funk1(this):
#     this("Hello World!")
#
# funk1(print)

# def func(num):
#     if num == 1:
#         return int    
#     elif num==0:
#         return print
#
# a=func(0)
# print(a)

def abc(func1):
    def executed():
        print("What Happened?")
        func1()
        print("Executed..")

    return executed


@abc                                    # method 2
def func1():
    print("Hello World")


# func1=abc(func1)                      #method 1
func1()
