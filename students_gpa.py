""" Matt Boyer 01/15/2023
ITEC 2905-80 Lab2
"""
# Import dataclasses
from dataclasses import dataclass

@dataclass
class Student:
    # Open string variable
    student_name: str
    # Open integer variable
    student_college_id: int
    # Float variable
    student_gpa: float

# Function to concatinate variables
    def __str__(self):
        # Returns concatination of variables as message
        return f'Name {self.student_name}, ID: {self.student_college_id}, GPA: {self.student_gpa}'          

def main():
    # Add input to get variables from user
    student_name = input('Enter students name: ')
    student_college_id = input(f'Enter {student_name}\'s Student ID: ')
    student_gpa = float(input(f'Enter {student_name}\'s GPA: ')) 


# Renaming Variables to (s), calling on Student class to assign variables to open 
    s = Student(student_name, student_college_id, student_gpa)

    # Utilizes def __str__(self) for printing return string statement
    print(s)

main()                      # Will not display/run without this line
print('End of program, Thank you')