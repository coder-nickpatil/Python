def Myfun(Normal, *args, **kwargs):  # RULE:NORMAL ARGUMENT ALWAYS 1ST THEN ARGS
    print(Normal)
    for item in args:
        print(item)
    print("\nNow I would like to introduce some students: ")
    for key, value in kwargs.items():
        print(f"The Name of Student is {key} & Role is {value}")


Normal = "Students Names:"
lst = ["Nikhil", "Rohan", "Pratik", "Shrish"]

kw = {"Nikhil": "Intructor", "Shirish": "Student", "Yash": "Co-ordinator"}
Myfun(Normal, *lst, **kw)
