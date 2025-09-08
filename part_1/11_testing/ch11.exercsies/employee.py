class Employee:
    """Models an employee's basic information and salary raise"""
    def __init__(self, first, last, salary):
        """Gives an instance of employee's basic information"""
        self.first = first
        self.last = last
        self.salary = []
        self.salary.append(salary)

    def give_raise(self, salary=5000):
        """Simulates salary raise"""
        self.salary.append(salary) 

    def show_salary(self):
        """Displays employee's salary history"""
        print(f"this employee's salary history is {self.salary}")

# emp1 = Employee('jon', 'doe', 1)
# emp1.show_salary()

# emp1.give_raise()
# emp1.show_salary()
