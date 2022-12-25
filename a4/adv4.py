text_file = open("input.txt", "r")
lines = text_file.read().splitlines()


def convert_to_range_pair(line):
    range_pair=[]
    for pairs in line:
        str_pair = pairs.split('-')
        range_pair.append(range(int(str_pair[0]),int(str_pair[1])+1))
    return range_pair

def setup_pair_array(in_lines):
    pair_array=[]
    for line in in_lines:
        pair_array.append(convert_to_range_pair(line.split(',')))
    return pair_array

def first_task():
    pair_array = setup_pair_array(lines)
    subset_count=0
    for range_pair in pair_array:
        if(set(range_pair[0]).issubset(set(range_pair[1])) or set(range_pair[1]).issubset(set(range_pair[0]))):
            subset_count+=1
    print(subset_count)

def second_task():
    pair_array = setup_pair_array(lines)
    subset_count=0
    for range_pair in pair_array:
        if(set(range_pair[0]).intersection(set(range_pair[1])) or set(range_pair[1]).intersection(set(range_pair[0]))):
            subset_count+=1
    print(subset_count)

first_task()
second_task()