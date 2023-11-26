import os



def ls(args.path=os.getcwd()):
    for (root,dirs,files) in os.walk(path, topdown=True):
        print(files)

def change_directory (args.path):
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
    
def remove_directory (args.path):
    for folder_name, subfolders, filenames in os.walk(path):
        if len(filenames) == 0 : # checkeing if it is empty or not
            os.remove(subfolders)
            print("deleted!")
            break 
        else:
            print(f"your folder : {subfolders} is not empty! ")

def remove_file (args.path , file):
    for folder_name , subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename == file :
                os.remove(file)
                print("deleted")
                break
            else:
                print("file dosent exsist!")

def removr_fdirectory(args.path):
    files = []
    for root, subfolders, filenames in os.walk(path):
        for filename in filenames :
            files.append(os.path.join(root, filenames ))
            if len(files) == 0:
                os.remove(subfolder)
            try :
                os.remove(files[0])
                files.pop[0]
            except OSError as error: 
                print("operating system error")
                continue

def create_dirs (args.path ,name):
    all_files = (os.listdir(os.curdir)).sort()
    count = 1
    for i in all_files:
        if "New Folder" in i: # if user didnt type the name for files
            count += 1
    name = f"folder_{name}" or f"New Folder ({count})"
    new_path = os.path.join(path, name)
    os.mkdir(new_path)

def output(file):
    for folder_name, subfolders, filenames in os.walk(file):
        print(filenames)
