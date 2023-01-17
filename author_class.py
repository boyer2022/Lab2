""" Matt Boyer 01/15/2023
ITEC 2905-80 Lab2
"""

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books: {titles}'

def main():
    tolkien = Author('J.R.R. Tolkien')
    tolkien.publish('The Hobbit')
    tolkien.publish('The Fellowship of the Rings')
    tolkien.publish('The Two Towers')
    tolkien.publish('The Return of the King')

    print(tolkien)

main()
print('End of program, Thank you')