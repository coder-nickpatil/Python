class Employee:
    """Constructor"""
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    """ Method of class """

    def PrintDetails(self):
        return f"My name is {self.name} , Salary is {self.salary} and Role is {self.role}"


harry = Employee("Harry",500,"Instructor")
nikhil = Employee("Nikhil",5000,"Student")

# harry.name = "Harry"
# harry.salary = 500
# harry.role = "Instructor"
#
# nikhil.name = "Nikhil"
# nikhil.salary = 1000
# nikhil.role = "Student"

print(harry.PrintDetails())
print(nikhil.PrintDetails())
print(harry.name)
print(harry.salary)
print(harry.role)