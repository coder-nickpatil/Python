class Employee:
    no_of_leaves = 8
    """Constructor"""

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    """ Method of class """

    def PrintDetails(self):
        return f"My name is {self.name} , Salary is {self.salary} and Role is {self.role}"

    @classmethod                                   #Decorator of class -> Use to change class methods
    def changeleaves(cls, newleaves):               #work like alternative constructor 
        cls.no_of_leaves = newleaves


harry = Employee("Harry", 500, "Instructor")
nikhil = Employee("Nikhil", 5000, "Student")

print(harry.no_of_leaves)
harry.changeleaves(4)
print(harry.no_of_leaves)
