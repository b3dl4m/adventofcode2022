class Directory:
    def __init__(self,parent_dir, name):
        self.parent_dir = parent_dir
        self.name = name
        self.directories = []
        self.files = []

class File:
    def __init__(self,name,size):
        self.name = name
        self.size = size

global root_directory
root_directory = Directory(None,"/")

def read_input():
    file = open("input.txt","r")
    global lines
    lines = file.read().splitlines()

def process_cmd(ins,curr_dir):
    print(ins)

def create_dir(ins,curr_dir):
    print(ins)

def create_file(ins,curr_dir):
    print(ins)

def process_inputs():
    curr_dir = root_directory
    for line in lines:
        ins = line.split()
        if(ins[0]=='$'):
            # instruction
            process_cmd(ins,curr_dir)
        elif(ins[0]=='dir'):
            # dir creation
            create_dir(ins)
        else:
            # file creation
            create_file(ins)



read_input()
process_inputs()
