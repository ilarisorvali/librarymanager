# librarymanager

librarymanager is a pseudo library book manager Python application that uses [rich](https://github.com/Textualize/rich) for it's terminal user interface.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) or [uv](https://docs.astral.sh/uv/) to install requirements.

With pip >= 23.1

```bash
pip install .
```
with uv
```bash
uv pip install
```

## Usage
```bash
python library.py path/to/csv/file.csv
```
If the file does not exist, one with the supplied name will be created when user adds a new book to the database.

After starting the program asks the user to select from three options:
1. Print the books on file to the terminal window
2. Add a new book from user input to the database file
3. Exit the program

After printing the information on disk or adding a new book, the program returns to the main menu, where the user is again presented with the same three options as on startup.

## License

[MIT](https://choosealicense.com/licenses/mit/)
