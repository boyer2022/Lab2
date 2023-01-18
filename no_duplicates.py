""" Matt Boyer 01/15/2023
ITEC 2905-80 Lab2
"""

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
       # Add duplication check
        if title not in self.books:
            self.books.append(title)
        else:
            print(f'{title} is in the list already. Please reenter a book title.')
       # Concatination string to send to main 
    def __str__(self):
        # Empty list check
        titles = ', '.join(self.books) or 'No published books'
        # Formatted string object
        return f'{self.name}. Books: {titles}'

def main():
    # User input for Author
    author_input = input('Enter an author: ')

    # Call for Author class with user input
    author = Author(author_input)
    author.publish(input(f'Enter a name of the book for {author_input}: '))
        # Enter more data to books[]
    question = input('Would you like to enter another book? Enter to quit.')
    # While loop as long as user inputs 'y'
    while question:
        # Calls publish function in Author class to append book title and add to book[]
        author.publish(input(f'Enter a name of the book for {author_input}: '))
        # Restate question for more titles
        question = input('Would you like to enter another book? Enter to quit.')
   
   # prints __str__ function formatted string
    print(author)
# Call to main
main()
# Output to user that program has stopped running
print('End of program, Thank you')
""" I am so happy with this! I was able to figure out how to loop a question to the user, only based on the example in the videos! """