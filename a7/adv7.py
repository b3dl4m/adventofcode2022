class File:
    def __init__(self,name:str,size:int):
        self.name:str = name
        self.size:int = size
class Directory:
    def __init__(self,parent_dir, name:str):
        self.parent_dir: Directory = parent_dir
        self.name:str = name
        self.directories:list[Directory] = []
        self.files:list[File] = []
        self.total_size = 0

global root_directory
curr_dir = None
root_directory = Directory(None,"/")

def change_directory(name) -> Directory:
    if(root_directory.name==name):
        global curr_dir
        curr_dir = root_directory
    else:
        recursive_kid_check(root_directory,name)

def recursive_kid_check(t_dir:Directory,name:str) -> Directory:
    if(t_dir.name==name):
        global curr_dir
        curr_dir = t_dir
    else:
        for dir in t_dir.directories:
            recursive_kid_check(dir,name)

def read_input():
    file = open("C:\Development\python\AOC2022\\adventofcode2022\\a7\input.txt","r")
    global lines
    lines = file.read().splitlines()

def process_cmd(ins):
    if(ins[1]=="cd"): #change directory
        change_directory(ins[2])

def create_dir(ins):
    curr_dir.directories.append(Directory(curr_dir,ins[1]))

def create_file(ins):
    curr_dir.files.append(File(ins[1],ins[0]))
    curr_dir.total_size+=int(ins[0])

def process_inputs():
    for line in lines:
        ins = line.split()
        if(ins[0]=='$'):
            # instruction
            if(ins[1]=="cd"): #process dir change
                process_cmd(ins)
        elif(ins[0]=='dir'):
            # dir creation
            create_dir(ins)
        else:
            # file creation
            create_file(ins)
    
def tree_print_out(disp_dir:Directory):
    print(disp_dir.name)
    for file in disp_dir.files:
        print("    - "+str(file.size)+" "+file.name)
    for dir in disp_dir.directories:
        tree_print_out(dir)

def dir_print_out(dir_name:str):
    change_directory(dir_name)
    print(curr_dir.name)
    for file in curr_dir.files:
        print("    - "+str(file.size)+" "+file.name)
    for dir in curr_dir.directories:
        print(dir.name)

def get_directory_size():
    print(root_directory.name+" size: "+str(root_directory.total_size))
    for dir in root_directory.directories:
        get_recursive_dir_size(dir)

def get_recursive_dir_size(dir:Directory):
    print(dir.name+" size: "+str(dir.total_size))
    for sub_dir in dir.directories:
        get_recursive_dir_size(sub_dir)

    
read_input()
process_inputs()
#tree_print_out(root_directory)
#dir_print_out("/")

def first_task():
    #find all directories and their total sizes
    get_directory_size()
    #find all the directories with with total size <= 100000

    print("hi")


first_task()