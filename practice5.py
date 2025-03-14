# 3. Difference Between Parameters and Attributes
# Problem: Employee Performance Review
# Create an Employee class that:
# Takes name, base_salary, and bonus_percentage as parameters.
# Stores name and base_salary as attributes.
# Uses a method calculate_bonus() to compute the bonus.
# Implements update_bonus(new_percentage) to change the bonus.

class Employee():
    def __init__(self, name, base_salary, bonus_percentage):
        self.name = name
        self.base_salary = base_salary

    def calculate_bonus(self, bonus_percentage):
        bonus = (self.base_salary * bonus_percentage) / 100
        return f"{self.name}'s bonus: {bonus}"
    
    def update_bonus(self, new_percentage):
          print(f"{self.name}'s bonus percentage updated to {new_percentage}%")
    

employee1 = Employee("Ayesha", 50000, 10)

print(employee1.calculate_bonus(10)) 

employee1.update_bonus(15)

print(employee1.calculate_bonus(15)) 

    
