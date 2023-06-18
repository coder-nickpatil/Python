# Instance variable is Instances own property...

class Employee:
    No_of_leaves = 8                  #class variable
    pass


harry = Employee()
nikhil = Employee()

harry.name = "Harry"
harry.salary = 500
harry.role = "Instructor"

nikhil.name = "Nikhil"
nikhil.salary = 1000
nikhil.role = "Student"

# print(harry.name)
# print(harry.salary)
# print(nikhil.role)

print(Employee.No_of_leaves)         #Main Class Common Property
print(harry.__dict__)
harry.No_of_leaves=9                 # Creates New Personal Instance Variable
print(harry.__dict__)
print(nikhil.No_of_leaves)


