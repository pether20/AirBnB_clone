#!/usr/bin/python3
"""
Class HBNBCCommand
"""
import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Interprete de comandos"""
    prompt = "(hbnb) "

    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_EOF(self, args):
        """Salir del interprete exit the program"""
        print("")
        return True

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def do_quit(self, args):
        """Salir del interprete exit the program"""
        return(True)

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_count(self, line_args_obj):
        args = line_args_obj.split()
        if args[0] not in classes:
            return
        else:
            count = 0
            keys = models.storage.all().keys()
            for key in keys:
                lenght = len(args[0])
                if key[:lenght] == args[0]:
                    count += 1
            print(count)

    def do_create(self, line):
        """Create a object"""
        if len(line) == 0:
            print("** class name missing **")
            return
        try:
            nueva_inst = HBNBCommand.class_dict[line]()
            nueva_inst.save()
            print(nueva_inst.id)
        except Exception as fail:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ print the instan str"""
        line_tokens = line.split()
        if len(line_tokens) == 0 or line is None:
            print("** class name missing **")
            return
        elif line_tokens[0] not in (HBNBCommand.class_dict.keys()):
            print("** class doesn't exist **")
        elif len(line_tokens) == 1:
            print("** instance id missing **")
        elif len(line_tokens) == 2:
            BM_id = f"{line_tokens[0]}.{line_tokens[1]}"
            if BM_id in models.storage.all():
                print(models.storage.all()[BM_id])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """ delete an object"""
        line_tokens = line.split()
        if len(line_tokens) == 0:
            print("** class name missing **")
        elif line_tokens[0] not in (HBNBCommand.class_dict.keys()):
            print("** class doesn't exist **")
        elif len(line_tokens[1]) == 0:
            print("** instance id missing **")
        elif len(line_tokens) == 2:
            BM_id = f"{line_tokens[0]}.{line_tokens[1]}"
            if BM_id in models.storage.all():
                del models.storage.all()[BM_id]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """ print the instan str"""
        class_prin = []
        line_tokens = line.split()
        if len(line_tokens) == 0:
            for obj in storage.all().values():
                class_prin.append(str(obj))
            print(class_prin)
        elif line_tokens[0] not in (HBNBCommand.class_dict.keys()):
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if line_tokens[0] == obj.__class__.__name__:
                    class_prin.append(str(obj))
            print(class_prin)

    def do_update(self, line):
        """ adding or updating attributes """
        line_tokens = line.split()
        id_token = line_tokens[0] + "." + line_tokens[1]
        if len(line_tokens) == 0:
            print("** class name missing **")
        elif line_tokens[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(line_tokens) == 1:
            print("** instance id missing **")
        elif id_token not in (storage.all().keys()):
            print("** no instance found **")
        elif len(line_tokens) == 2:
            print("** attribute name missing **")
        elif len(line_tokens) == 3:
            print("** value missing **")
        else:
            all_objs = storage.all()
            cr_obj = all_objs[id_token]
            setattr(
                cr_obj,
                line_tokens[2],
                line_tokens[3]
            )
            cr_obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
