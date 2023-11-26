import datetime
import argparse
import shutil
import sys
import os
def setup():
    parser = argparse.ArgumentParser(description= "CLI Tool for File Manipulation")
    parser.add_argument("--ls", type= str, help= "show the directories!")
    parser.add_argument("--cd", type= str, help= "change the working directory!")
    parser.add_argument("--mkdir", type= str, help= "create new directory!")
    parser.add_argument("--rmdir", type= str, help= "remove the directory if its empty!")
    parser.add_argument("--rm", type= str, help= "remove the file!")
    parser.add_argument("--rm-r", type=str, help= "remove the directory!")
    parser.add_argument("--cp", nargs= "+", type= str, help= "copy a file or directory!")
    parser.add_argument("--mv", nargs= "+", type= str, help= "move a file or directory!")
    parser.add_argument("--find", nargs= "+", type= str, help= "search for files or directories!")
    parser.add_argument("--cat", type= str, help= "Output the contents of the file!")
    parser.add_argument("--show-logs",action="store_true", help="show all logs of the program")
    parser.add_argument("--path" ,type= str , help="get the path of directory")
    parser.add_argument("--name" ,type= str , help="get the name for file")
    return parser

def copy(list_copy):
    source = list_copy[0]
    destination = list_copy[1]
    try:
        shutil.copy(source, destination)
        print(f"{source} copied to {destination}!")
    except shutil.SameFileError:
        print("Source and destination represents the same file.")
    except:
        print("Error occurred while copying file.")

def move(list_move):
    source = list_move[0]
    destination = list_move[1]
    try:
        shutil.move(source, destination)
        print(f"{source} moved to {destination}!")
    except shutil.SameFileError:
        print("Source and destination represents the same file.")
    except:
        print("Error occurred while moving file.")

def find(list_find):
    if len(list_find) == 1:
        find_file(list_find)
    else:
        find_exts(list_find)

def find_file(list_find):
    filename = list_find[0]
    for p, dir, file in os.walk('/'):
        if filename in file:
            print(os.path.join(p, filename))
        else:
            print(f"{filename} --> not found!")

def find_exts(list_find):
    path = list_find[0]
    ext = list_find[1]
    exts = ()
    for p, dir, file in os.walk(path):
        for f in file:
            _, ext1 = os.path.splitext(f)
            exts.add(ext1)
            if ext in exts:
                print(os.path.join(p, f))

def log_command(line):
    with open("commands.log", "a") as file:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d")
        file.write(f"{time_now}: {line}\n")
  
def show_logs():
    with open("commands.log", "r") as file:
        print(file.read())

def ls(path=os.getcwd()):
    for (root,dirs,files) in os.walk(path, topdown=True):
        print(files)

def change_directory (path):
    path = str((os.walk(path)))
    current = os.getcwd()
    desktop_path = os.path.join(current,path)
    os.chdir(desktop_path)
    print("Directory changed")

    """
    another way for changing directory
    os.system(f'cd {str((os.walk(path)))}')
    print("Directory changed")
    """
    
def remove_directory (path):
    for folder_name, subfolders, filenames in os.walk(path):
        if len(filenames) == 0 : # checkeing if it is empty or not
            os.remove(subfolders)
            print("deleted!")
            break 
        else:
            print(f"your folder : {subfolders} is not empty! ")

def remove_file (path ,name):
    for folder_name , subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename == file :
                os.remove(name)
                print("deleted")
                break
            else:
                print("file dosent exsist!")

def remove_fdirectory(path):
    files = []
    for root, subfolders, filenames in os.walk(path):
        for filename in filenames :
            files.append(os.path.join(root, filenames ))
            if len(files) == 0:
                os.remove(subfolder) # another way =======> shutil.rmtree(subfolder)
            try :
                os.remove(files[0])
                files.pop[0]
            except OSError as error: 
                print("operating system error")
                continue

def create_dirs (path ,name):
    all_files = os.listdir(os.curdir)
    all_files.sort()
    count = 1
    for i in all_files:
        if "New Folder" in i: # if user didnt type the name for files
            count += 1
    name = f"folder_{name}" or f"New Folder ({count})"
    new_path = os.path.join(path, name)
    os.mkdir(new_path)

def output(name):
    for path, subfolders, filenames in os.walk(name):
        filelist1 = os.listdir(path)
        filelist1.sort()   # sort alphabetically
        #filelist1 = os.listdir(os.curdir) ======> current folder (directory)
        print(filelist1) 

#--------------------------------MAIN------------------------------------------
cms = setup()
args = cms.parse_args()
command_line = " ".join(sys.argv)
log_command(command_line)
list_move = args.mv
list_copy = args.cp 
list_find = args.find 
if args.ls:
    ls(path = os.getcwd())
elif args.cd:
    change_directory(path)
elif args.mkdir:
    create_dirs(path)
elif args.rmdir:
    remove_directory(path)
elif args.rm:
    remove_file(path,file)
elif args.rm_r:
    remove_fdirectory(path)
elif args.cp:
    copy(list_copy)
elif args.mv:
    move(list_move)
elif args.find:
    find(list_find)
elif args.cat:
    output(File)
elif args.show_logs:
    show_logs()
