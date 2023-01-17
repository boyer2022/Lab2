""" Matt Boyer 01/15/2023
ITEC 2905-80 Lab2
"""
# Import dataclasses
from dataclasses import dataclass

@dataclass
class Student:
    # Open string variable
    name: str
    # Open integer variable
    college_id: int
    # Float variable
    gpa: float

# Function to concatinate variables
    def __str__(self):
        # Returns concatination of variables as message
        return f'Name {self.name}, ID: {self.college_id}, GPA: {self.gpa}'          

def main():
    # TODO Add input to get variables from user
    alice = Student('Alice', 12345, 4.0)
    bob = Student('Bob', 98765, 3.2)

# Printing the concatinated String message for each student
    print(alice)
    print(bob)

main()                      # Will not display/run without this line