#!/usr/bin/env python3

# Standard library imports
import datetime
from collections import OrderedDict
import sys
import os


# Custom imports
from appdirs import user_data_dir
from peewee import *


# Choose application local data location in a platform independent manner
appname = "ConsoleLogbook"
data_dir = user_data_dir(appname, "")

# Create data directory if not exists
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Join path in a platform independent manner
db_path = os.path.join(data_dir, 'console_logbook_database.db')

# Create sqlite database
db = SqliteDatabase(db_path)


# Define Peewee model
class Entry(Model):

    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    # id field automatically created as primary key

    class Meta:
        database = db


def initialize():
    """ Create database and tables if non-existent """
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """ Main menu loop """
    choice = None

    # Loop over options as long as user doesn't quit
    while choice != 'q':

        # Loop over menu items and render each
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))  # Fetch function docstring and print it

        # Get user input
        choice = input("Action: ").lower().strip()
        print("\n")

        # Call user-chosen function
        if choice in menu:
            menu[choice]()


def add_entry():
    """ Add a logbook entry """

    print("-------------------------------------------------\n" +
          "Enter your entry. Press [ctrl + d] when finished.\n" +
          "-------------------------------------------------\n")

    # Read user data
    data = sys.stdin.read().strip()

    # If data non-empty save entry to database
    if data:
        if input('Save entry? [y/n]').lower().strip() == 'y':
            Entry.create(content=data)
            print("Saved successfully!\n")


def view_entries(search_query=None):
    """ View previous entries """

    # Select all entries
    query = Entry.select().order_by(Entry.timestamp.desc())

    # If search query is not None, only select entries containing string
    if search_query:
        query = query.where(Entry.content.contains(search_query))

    # Loop over entries and print out contents and timestamp
    for entry in query:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(timestamp)
        print('=' * len(timestamp))
        print(entry.content)
        print("\n")
        print('n) next entry')
        print('d) delete entry')
        print('q) return to main menu')
        action = input('Action: ').lower().strip()
        if action == 'q':
            break
        elif action == 'd':
            delete_entry(entry)
        print("\n")

def search_entries():
    """ Search entries for a string """

    view_entries(input('Search query: '))


def delete_entry(entry):
    """ Delete certain entry """
    if input("Are you sure you want to delete this? [y/n]").lower().strip() == 'y':
        entry.delete_instance()
        print("------------\nEntry deleted.\n------------\n")


# Switch-statement like syntax for menu construction
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
])


if __name__ == '__main__':
    initialize()
    menu_loop()
