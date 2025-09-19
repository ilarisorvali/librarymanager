from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm

from dataclasses import dataclass
import csv
import os
import argparse

#Filename for the books csv "database"
FILENAME = "library.csv"
console = Console()

#Dataclass to hold book information in memory, offers nice sorting capabilities.
@dataclass(order=True)
class Book:
    title: str
    author: str
    isbn: int
    year: int

#Read books from database file and return as a list of Book objects.
def read_books(filename: str) -> list[Book]:
    books: list[Book] = []
    if os.path.exists(filename):
        with open(filename, newline='') as libraryfile:
            reader = csv.reader(libraryfile)
            for row in reader:
                #Check if row includes all information necessary
                if len(row) == 4:
                    #Extract information from row
                    title, author, isbn, year = row
                    books.append(Book(title.strip(), author.strip(), int(isbn.strip()), int(year.strip())))

    #Return books read from file
    return books

#Takes a list of books and writes them to database file sorted by year
def write_books(filename: str, books: list[Book]) -> None:
    with open(filename, "w", newline='') as libraryfile:
        writer = csv.writer(libraryfile)
        #Sort books in memory and write to file
        for book in sorted(books, key=lambda book: book.year):
            writer.writerow([book.title, book.author, book.isbn, book.year])

#Takes a list of books and displays them to the user using rich library Table
def display_books(books: list[Book]) -> None:
    table = Table(title="Library content", show_lines=True)
    table.add_column("Title", style="cyan", no_wrap=True)
    table.add_column("Author", style="magenta")
    table.add_column("ISBN", style="magenta")
    table.add_column("Year", style="magenta")

    for book in books:
        table.add_row(book.title, book.author, str(book.isbn), str(book.year))

    console.print(table)

#Add a book to the database file from user input, asks for confirmation from the user.
def add_book(filename: str, books: list[Book]) -> None:

    title = Prompt.ask("Enter book title")
    author = Prompt.ask("Enter book author")
    #IntPrompt for type safety
    year = IntPrompt.ask("Enter book publishing year")
    isbn = IntPrompt.ask("Enter book ISBN")

    dbConfirmation = Confirm.ask("[bold yellow]Do you want to write this book information to the database file?")

    if dbConfirmation:
        books.append(Book(title, author, int(isbn), int(year)))
        #Sort and write books to file
        write_books(filename, books)
        console.print("[bold green]Wrote book information to database file!")
    else:
        console.print("[bold red]Book information discarded. Nothing written to database.")

def main():
    parser = argparse.ArgumentParser(description="Book CSV library")
    parser.add_argument("filename", help="Path to the CSV database file.")
    args = parser.parse_args()

    filename: str = args.filename

    while True:
        console.print("\nMain Menu \nChoose action from below (1-3).")
        #Show command options
        console.print("1. Print book database (default)")
        console.print("2. Add a new book to database")
        console.print("3. Exit the program")
        #Read books from the databse file to pass onto display or adding function.
        books = read_books(filename)

        choice = Prompt.ask("Choose an option", choices=["1", "2", "3"], default="1")

        if choice == "1":
            display_books(books)
        elif choice == "2":
            add_book(filename, books)
        elif choice == "3":
            console.print("[bold green]Goodbye![/bold green]")
            break


if __name__ == "__main__":
    main()
