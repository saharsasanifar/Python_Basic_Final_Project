import os
def ls(path):
    for (root,dirs,files) in os.walk(path, topdown=True):
        print(files)






def create_directory (path):
    path = str((os.walk(path)))
    current = (os.getcwd())
    desktop_path = os.path.join(current,path)
    os.chdir(desktop_path)
    print("Directory changed")
    
 




def remove_directory (path):
    for folder_name, subfolders, filenames in os.walk(path):
        if len(filenames) == 0 :
            os.remove(subfolders)
            print("deleted!") 
        else:
            print(f"your folder : {subfolders} is not empty! ")


def removr_file (path , file):
    for folder_name , subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename == file :
                os.remove(file)
                print("deleted")
            else:
                print("file dosent exsist!")

def removr_fdirectory(path):
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
                ...


def create_dirs (path ,name):
    name = f"folder_{name}"
    new_path = os.path.join(path, name)
    os.mkdir(new_path)


def output(file):
    for folder_name, subfolders, filenames in os.walk(file):
        print(filenames)

    


    