#!/usr/bin/python3

import sys

class Console:
    def __init__(self):
        self.prompt = "(hbnb) "

    def help(self):
        print("\nDocumented commands (type help <topic>):")
        print("=" * 40)
        print("EOF  help  quit")
        print()

    def loop(self):
        while True:
            try:
                command = input(self.prompt)
            except EOFError:
                break
            
            if command.strip() == 'quit':
                break
            elif command.strip() == 'help':
                self.help()

    def non_interactive(self):
        self.help()
        self.loop()

if __name__ == "__main__":
    console = Console()

    if sys.stdin.isatty():
        console.loop()
    else:
        console.non_interactive()

