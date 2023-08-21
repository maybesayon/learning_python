class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"Name is {self.name} and age is {self.age}"

class Employee(Person):
    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation

    def description(self):
        print(super().description())
        return f"Salary is {self.salary} and designation is {self.designation}"


Employee = Employee("John", 30, 100000000, "Manager")
print(Employee.description())
