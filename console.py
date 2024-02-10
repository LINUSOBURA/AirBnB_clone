#!/usr/bin/python3

import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel"]
    
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

    def do_create(self, arg):
        '''Create a new instance of BaseModel'''
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new = eval(arg)()
        new.save()
        print(new.id)

    def do_show(self, arg):
       '''Prints the string representation of an instance'''
       args = arg.split()
       if not args:
            print("** class name missing **")
            return
       if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
       if len(args) == 1:
           print("** instance id missing **")
           return
       key = args[0] + '.' + args[1]
       all_objs = models.storage.all()
       if key in all_objs:
           print(all_objs[key])
       else:
           print("** no instance found **")

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id'''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        all_objs = models.storage.all()
        if key in all_objs:
            del all_objs[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        '''Prints all string representation of all instances'''
        args = arg.split()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        objs_list = []
        all_objs = models.storage.all()
        for obj_key in all_objs:
            if not args or all_objs[obj_key].__class__.__name__ == args[0]:
                objs_list.append(str(all_objs[obj_key]))
        print(objs_list)

    def do_update(self, arg):
        '''Updates an instance based on the class name and id'''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        all_objs = models.storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(all_objs[key], args[2], args[3])
        all_objs[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
