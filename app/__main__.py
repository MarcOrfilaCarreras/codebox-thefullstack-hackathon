# -*- coding: utf-8 -*-
import sys

from .commands import add
from .commands import delete
from .commands import list
from .utils import messages


def cli():
    # Check if there are at least 2 command line arguments (including the script name)
    if len(sys.argv) < 2:
        print(messages.help_default())  # Print the default help message
        return  # Exit the function if no valid subcommand is provided

    subcommand = sys.argv[1]  # Get the subcommand from the second argument
    args = sys.argv[2:]  # Get the remaining arguments as a list

    if subcommand == "add":
        add.add(args)  # Call the 'add' function from the 'commands' module
    elif subcommand == "list":
        list.list()  # Call the 'list' function from the 'commands' module
    elif subcommand == "delete":
        # Call the 'delete' function from the 'commands' module
        delete.delete(args)
    elif subcommand == "help":
        print(messages.help_default())  # Print the default help message
    else:
        # Print an error message for an invalid subcommand
        print(messages.error_invalid_subcommand())


if __name__ == "__main__":
    cli()  # Call the 'cli' function when the script is executed directly
