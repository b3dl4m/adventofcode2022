def setup_stack():
    text_file = open("initial_stack.txt", "r")
    lines = text_file.read().splitlines()
    index_array=range(1,10)
    real_index_array = []
    big_string_array=[]
    for line in lines:
        big_string_array.append(list(line))

    big_string_array.reverse()
    for i in index_array:
        real_index_array.append(big_string_array[0].index(str(i)))
    
    stack_array=[]
    no_index_plz = 1
    for i in real_index_array:
        stack = []
        for line in big_string_array:
            if line[i]!=' ' and line[i]!=str(no_index_plz):
                stack.append(line[i])
        no_index_plz+=1
        stack_array.append(stack)
    
    return stack_array

stack_array = setup_stack()

def setup_instructions():
    text_file = open("just_instructions.txt", "r")
    lines = text_file.read().splitlines()
    out_lines=[]
    for line in lines:
        line=line.replace('move ','')
        line=line.replace('from ','')
        line=line.replace('to ','')
        line=line.split()
        out_lines.append(line)
    return out_lines

instructions = setup_instructions()

def process_instruction(how_many,where_from,to):
    for i in range(how_many):
        hold_this = stack_array[where_from-1].pop()
        stack_array[to-1].append(hold_this)

def process_multi_instruction(how_many, where_from, to):
    stack = []
    for i in range(how_many):
        hold_this = stack_array[where_from-1].pop()
        stack.append(hold_this)

    stack.reverse()
    stack_array[to-1]+=stack

def first_task():
    answer=''
    for instruction in instructions:
        process_instruction(int(instruction[0]),int(instruction[1]),int(instruction[2]))
    
    for line in stack_array:
        answer+=line[len(line)-1]

    print(answer)

def second_task():
    answer=''
    for instruction in instructions:
        process_multi_instruction(int(instruction[0]),int(instruction[1]),int(instruction[2]))
    
    for line in stack_array:
        answer+=line[len(line)-1]

    print(answer)


second_task()