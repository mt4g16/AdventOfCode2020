# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 00:41:15 2020

@author: Matteo
"""

my_file = open("input.txt", "r")
content = my_file.read()
sequence = content.split("\n")
my_file.close()

sequence = [int(i) for i in sequence]

#print(sequence)

#test = [1, 2, 3, 4, 5]

def possible_sums(extract):
    sums = []
    
    for index_i, i in enumerate(extract):
        for index_j, j in enumerate(extract):
            if index_i != index_j:
                sums.append(i + j)

    return sums

def check_number(preamble_length, sequence):
    
    seq_len = len(sequence)
    
    index = 0
    
    for num_index in range(preamble_length, seq_len):
        if sequence[num_index] in possible_sums(sequence[index:index+preamble_length]):
            index += 1
        else:
            print('Incongruent number: ' + str(sequence[num_index]) + ' at pos: ' + str(num_index))
            return sequence[num_index], num_index


def find_seq_sum(target_num, preamble_length, sequence):
    
    del sequence[check_number(preamble_length, sequence)[1]]
    
    seq_len = len(sequence)
    
    range_size = 2
        
    while True:
        for i in range(seq_len-1):
            if sum(sequence[i:i+range_size]) == target_num:
                key = sequence[i:i+range_size]
                print('Range size checked: ' + str(range_size))
                return max(key) + min(key)
                
        range_size += 1


print(find_seq_sum(check_number(25, sequence)[0], 25, sequence))
