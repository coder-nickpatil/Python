class Employee:
    no_of_leaves = 8

    """Constructor"""
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    """ Method of class """
    def PrintDetails(self):
        return f"My name is {self.name} , Salary is {self.salary} and Role is {self.role}."

    @classmethod                                   #Decorator of class -> Use to change class methods
    def changeleaves(cls, newleaves):               #work like alternative constructor
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls,string):
        """Method 1"""
        # params= string.split("-")
        # print(params)                              # Print list Splited
        # return cls(params[0],params[1],params[2])
        """Method 2"""
        return cls(*string.split("-"))

harry = Employee("Harry", 500, "Instructor")
nikhil = Employee("Nikhil", 5000, "Student")
rohan= Employee.from_str("Rohan-200-Coordinator")

# print(rohan.PrintDetails())

rohan.PrintGood("Nikhil")