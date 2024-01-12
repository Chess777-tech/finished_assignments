class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        # Method to give a raise to the employee
        self.salary += amount
        print(f"{self.name} received a raise. New salary: ${self.salary}")

    def display_details(self):
        # Method to display employee details
        print(f"Employee Details:")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")

# Example usage:
employee1 = Employee("John Doe", "Software Engineer", 80000)
employee2 = Employee("Jane Smith", "Data Scientist", 90000)

employee1.display_details()
employee2.display_details()

employee1.give_raise(5000)
employee2.give_raise(10000)

employee1.display_details()
employee2.display_details()