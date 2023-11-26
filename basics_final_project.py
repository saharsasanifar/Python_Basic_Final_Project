import datetime
import argparse
import shutil
import sys
import os
def setup():
    parser = argparse.ArgumentParser(description= "CLI Tool for File Manipulation")
    parser.add_argument("--ls", action= "store_true", help= "show the directories!")
    parser.add_argument("--cd", action= "store_true", help= "change the working directory!")
    parser.add_argument("--mkdir", action= "store_true", help= "create new directory!")
    parser.add_argument("--rmdir", action= "store_true", help= "remove the directory if its empty!")
    parser.add_argument("--rm", action= "store_true", help= "remove the file!")
    parser.add_argument("--rm-r", action= "store_true", help= "remove the directory!")
    parser.add_argument("--cp", nargs= "+", type= str, help= "copy a file or directory!")
    parser.add_argument("--mv", nargs= "+", type= str, help= "move a file or directory!")
    parser.add_argument("--find", nargs= "+", type= str, help= "search for files or directories!")
    parser.add_argument("--cat", action= "store_true", help= "Output the contents of the file!")
    parser.add_argument("--show-logs",action="store_true", help="show all logs of the program")
    return parser

def copy(args):
    source = args[0]
    destination = args[1]
    try:
        shutil.copy(source, destination)
        print(f"{source} copied to {destination}!")
    except shutil.SameFileError:
        print("Source and destination represents the same file.")
    except:
        print("Error occurred while copying file.")

def move(args):
    source = args[0]
    destination = args[1]
    try:
        shutil.move(source, destination)
        print(f"{source} moved to {destination}!")
    except shutil.SameFileError:
        print("Source and destination represents the same file.")
    except:
        print("Error occurred while moving file.")

def find(args):
    if len(args) == 1:
        find_file(args.find)
    else:
        find_exts(args.find)

def find_file(args):
    filename = args[0]
    for p, dir, file in os.walk('/'):
        if filename in file:
            print(os.path.join(p, filename))
        else:
            print(f"{filename} --> not found!")

def find_exts(args):
    path = args[0]
    ext = args[1]
    exts = ()
    for p, dir, file in os.walk(path):
        for f in file:
            _, ext1 = os.path.splitext(f)
            exts.add(ext1)
            if ext in exts:
                print(os.path.join(p, file))

def log_command(line):
    with open("commands.log", "a") as file:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d")
        file.write(f"{time_now}: {line}\n")

    
def show_logs():
    with open("commands.log", "r") as file:
        print(file.read())
#MAIN----------------------------------------------
cms = setup()
args = cms.parse_args()
command_line = " ".join(sys.argv)
log_command(command_line)
if args.ls:
    pass
elif args.cd:
    pass
elif args.mkdir:
    pass
elif args.rmdir:
    pass
elif args.rm:
    pass
elif args.rm_r:#if you see this so it means that your in hurry and i cant say this to you it has Error with dash
    pass
elif args.cp:
    copy(args.cp)
elif args.mv:
    move(args.mv)
elif args.find:
    find(args.find)
elif args.cat:
    pass
elif args.show_logs:
    show_logs()
