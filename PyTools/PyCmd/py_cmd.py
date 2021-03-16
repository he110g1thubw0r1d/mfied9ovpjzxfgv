# PyCmd v1.0-alpha.2(a210316)
from time import sleep
uppercase = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
files = {}
working_dir = None
directory_count = None
disk_list = []
location = None


def ls(command):
    directory_count = working_dir["DIR_COUNT"]
    print(
        f"{(len(working_dir)-1)-directory_count} Files, {directory_count} Directories"
    )
    if (len(working_dir) - 1) != 0:
        print(" ".join(working_dir.keys())[10:])


def touch(command):
    global files, location
    argument = command[6:]
    if "." not in argument:
        argument += ".txt"
    working_dir[argument] = ""


def rm(command):
    global working_dir
    argument = command[3:]
    if argument not in working_dir.keys():
        print("Invalid file")
        return
    if dict(working_dir[argument]):
        print("Use 'rmdir' command to remove a directory.")
        return
    del working_dir[argument]
def cd(command):
    global location
    argument = command[3:]
    if (argument == "..") and (location[1:] != ":\\"):
        location = "\\".join(location.split("\\")[:-1])
        return
    if argument not in (working_dir.keys()):
        print("Invalid directory")
        return
    if location[1:] != ":\\":
        location += "\\"
    location += argument


def rmdir(command):
    global files, location, working_dir
    argument = command[6:]
    if (argument not in working_dir.keys()):
        print("Invalid directory")
        return
    if not dict(working_dir[argument]):
        print("Use 'rm' command to remove a file.")
        return
    del working_dir[argument]
    files[location]["DIR_COUNT"] -= 1


def add_disk():
    global files, disk_list
    argument = input("Enter disk name(Only one uppercase letter allowed): ")
    if (argument in uppercase) and (len(argument) == 1):
        if argument in disk_list:
            print(f"The disk '{argument}' is already in the list.")
        else:
            disk_list.append(argument)
            files[argument + ":\\"] = {"DIR_COUNT": 0}
    else:
        print("Invalid disk name")
# PyCmd v1.0-alpha.2(a210316)
from time import sleep
upper_case = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
files = {}
working_dir = None
directory_count = None
disk_list = []
location = None


def ls(command):
    directory_count = working_dir["DIR_COUNT"]
    print(
        f"{(len(working_dir)-1)-directory_count} Files, {directory_count} Directories"
    )
    if (len(working_dir) - 1) != 0:
        print(" ".join(working_dir.keys())[10:])


def touch(command):
    global files, location
    argument = command[6:]
    if "." not in argument:
        argument += ".txt"
    working_dir[argument] = ""


def rm(command):
    global working_dir
    argument = command[3:]
    if argument not in working_dir.keys():
        print("Invalid file")
        return
    if dict(working_dir[argument]):
        print("Use 'rmdir' command to remove a directory.")
        return
    del working_dir[argument]
def cd(command):
    global location
    argument = command[3:]
    if (argument == "..") and (location[1:] != ":\\"):
        location = "\\".join(location.split("\\")[:-1])
        return
    if argument not in (working_dir.keys()):
        print("Invalid directory")
        return
    if location[1:] != ":\\":
        location += "\\"
    location += argument


def rmdir(command):
    global files, location, working_dir
    argument = command[6:]
    if (argument not in working_dir.keys()):
        print("Invalid directory")
        return
    if not dict(working_dir[argument]):
        print("Use 'rm' command to remove a file.")
        return
    del working_dir[argument]
    files[location]["DIR_COUNT"] -= 1


def add_disk():
    global files, disk_list
    argument = input("Enter disk name(Only one upper_case letter allowed): ")
    if (argument in upper_case) and (len(argument) == 1):
        if argument in disk_list:
            print(f"The disk '{argument}' is already in the list.")
        else:
            disk_list.append(argument)
            files[argument + ":\\"] = {"DIR_COUNT": 0}
    else:
        print("Invalid disk name")


def open_disk(disk_name):
    global files, location, working_dir
    location = disk_name + ":\\"
    working_dir = files[disk_name + ":\\"]
    while True:
        if location[-1] == ":":
            location += "\\"
        command = input("$ ")
        if command == "ls":
            ls(command)
        elif command == "pwd":
            print(location)
        elif "touch " in command:
            touch(command)
        elif "rm " in command:
            rm(command)
        elif "mkdir " in command:
            argument = command[6:]
            files[location][argument] = {"DIR_COUNT": 0}
            files[location]["DIR_COUNT"] += 1
        elif "cd " in command:
            cd(command)
            working_dir = files[disk_name + ":\\"]
            if location[1:] != ":\\":
                for element in location.split("\\")[1:]:
                    working_dir = working_dir[element]
        elif "rmdir " in command:
            rmdir(command)
        elif command == "exit":
            break
        else:
            print("Invalid command")


def remove_disk(disk):
    global files, disk_list
    if (disk in upper_case) and (len(disk) == 1):
        if disk not in disk_list:
            print(f"The disk '{disk}' is not in the list.")
        else:
            del files[disk]
            disk_list.remove(disk)
    else:
        print("Invalid disk name")


def run():
    global files, disk_list
    file = open("data.txt", "r")
    username = file.readline()[:-1]
    if username == "(null)":
        print("Error: No user\nOpen data.txt and replace (null) with your username.")
        sleep(15)
        return
    if file.readline()[-5:-1] == "True":
        new_user = True
    else:
        new_user = False
    files = eval(file.readline())
    file.close()
    print("PyCmd\n----------")
    if new_user == True:
        print(f"Welcome {username}!")
    else:
        print(f"Welcome back {username}!")
    disk_list = [disk[0] for disk in files.keys()]
    action_index = None
    while True:
        action = input(
            "Select action:\n1. Add Disk(add, AD, or 1)\n2. Open Disk(open, OD, or 2)\n3. Remove Disk(remove, RD, or 3)\n4. Show Disk List(show_list, SDL, or 4)\n5. Save And Quit(quit, SAQ, or 5)\n> "
        ).lower()
        action_list = [["add", "ad", "1"], ["open", "od", "2"],
                       ["remove", "rd", "3"], ["show_list", "sdl", "4"],
                       ["quit", "saq", "5"]]
        
        for i in range(len(action_list)):
            if action in action_list[i]:
                action_index = i
                break
        else:
            print("Invalid action")
            action_index = None
        if action_index == 0:
            add_disk()
        elif action_index == 1:
            argument = input("Enter disk name: ")
            if (argument in upper_case) and (len(argument) == 1):
                if argument in disk_list:
                    open_disk(argument)
                else:
                    print(f"The disk '{argument}' is not in the list.")
            else:
                print("Invalid disk name")
        elif action_index == 2:
            remove_disk(input("Enter disk name(Program will remove it): "))
        elif action_index == 3:
            print(", ".join(disk_list))
        elif action_index == 4:
            print("Bye!")
            break
    file = open("data.txt", "w")
    file.write(username + "\n")
    file.write("New user: False" + "\n")
    file.write(str(files))
    file.close()
    sleep(3)


run()
