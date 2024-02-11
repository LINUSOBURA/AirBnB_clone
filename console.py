#!/usr/bin/python3

import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import sys

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
    
    def do_create(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in FileStorage.classes():
            print("** class doesn't exist **")
            return
        new_instance = FileStorage.classes()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in FileStorage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = FileStorage.all()
        key = "{}.{}".format(class_name, args[1])
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in FileStorage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = FileStorage.all()
        key = "{}.{}".format(class_name, args[1])
        if key in objs:
            del objs[key]
            FileStorage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        '''Prints all string representation of all instance'''
        args = line.split()
        objs = FileStorage.all()
        result = []

        if len(args) == 0:
            for obj_id, obj in objs.items():
                result.append(str(obj))
            print(result)
        elif args[0] in FileStorage_classes:
            for obj_id, obj in objs.items():
                if obj.__class__.__name__ == args[0]:
                    result.append(str(obj))
            print(result)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        '''Updates an instance based on the class name and id'''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in FileStorage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = FileStorage.all()
        key = "{}.{}".format(class_name, args[1])
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objs[key], args[2], eval(args[3]))
        FileStorage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
