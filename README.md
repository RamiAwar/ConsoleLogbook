# ConsoleLogbook
A python-based platform-independent console application that allows saving entries in locally a logbook or diary fashion.

## Functionality
- Adding entries
- Deleting entries
- Viewing entries

## Requirements and Dependencies
- Requires Python 3.5+.
- Depends on `peewee`. To install with pip:
``` 
pip install peewee 
```

## Running the program
After installing requirements and dependencies, open up terminal/command-prompt and enter:
```
python3 console_logbook.py
```

## Description

This program uses Peewee ORM to create and manage a local SQLite database using Python. The program allows logging timestamped entries, viewing them at a later date, and deleting them when needed.

## Acknowledgements

This programs depends on ```appdirs.py``` which was created by ActiveState Software Inc. for locating the most suitable data storage locations across different platforms. Source: https://github.com/ActiveState/appdirs/ 
