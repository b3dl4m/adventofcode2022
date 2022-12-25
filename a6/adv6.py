text_file = open("input.txt", "r")
buffer = text_file.read()

def start_of_packet(in_buffer):
    for index in range(0,len(in_buffer)):
        potential_packet = in_buffer[index]+in_buffer[index+1]+in_buffer[index+2]+in_buffer[index+3]
        if(len(potential_packet)==len(set(potential_packet))):
            print(potential_packet)
            return index+4 # because of the index offset

def first_task():
    print("first task")
    answer = start_of_packet(buffer)
    print(answer)


# first_task()

def start_of_message(in_buffer):
    for index in range(0,len(in_buffer)):
        potential_message = in_buffer[index:index+14]
        if(len(potential_message)==len(set(potential_message))):
            print(potential_message)
            return index+14
    
def second_task():
    print("second task")
    answer = start_of_message(buffer)
    print(answer)

second_task()