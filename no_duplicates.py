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
# TODO 

    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books: {titles}'

def main():
    # author_input = input('Enter an author: ')

    # author = Author(author_input)
    # author.publish = input(f'Enter a name of the book for {author_input}: ')
    """ Using user input works but still displays NO PUBLISHED BOOKS """
    
    tolkien = Author('J.R.R. Tolkien')
    tolkien.publish('The Fellowship of the Rings')
    tolkien.publish('The Two Towers')
    tolkien.publish('The Return of the King')
    tolkien.publish('The Hobbit')
    tolkien.publish('The Hobbit')
    
    print(tolkien)
    # print(author)

main()
print('End of program, Thank you')