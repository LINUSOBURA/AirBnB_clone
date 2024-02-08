#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def emptyline(self):
        pass

    def do_EOF(self, line):
        '''End program with ctrl D'''
        return True

    def do_quit(self, line):
        '''quit to end program'''
        return True

    def default(self, line):
        print("Unkown command {}".format(line))



if __name__ == '__main__':
    HBNBCommand().cmdloop()
