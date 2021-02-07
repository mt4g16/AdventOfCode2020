# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 23:52:11 2020

@author: Matteo
"""

my_file = open("input.txt", "r")
content = my_file.read()
instructions = content.split("\n")
my_file.close()

#print(instructions)

def detect_instruction(ins):
    ins = ins.split(' ')
    ins_chg = 0
    
    if ins[1][0] == '+':
        ins_chg = int(ins[1][1:])
    if ins[1][0] == '-':
        ins_chg = -1 * int(ins[1][1:])
    
    if ins[0] == 'acc':
        return 'acc', ins_chg
    
    if ins[0] == 'nop':
        return 'nop', ins_chg
    
    if ins[0] == 'jmp':
        return 'jmp', ins_chg

def run(full_ins):
    repeat_check = [0] * len(full_ins)
    
    index = 0
    acc = 0
    
    while all(i < 2 for i in repeat_check):
        ins_type = detect_instruction(full_ins[index])
        
        if ins_type[0] == 'acc':
            acc += ins_type[1]
            index += 1
        
        if ins_type[0] == 'nop':
            index += 1
        
        if ins_type[0] == 'jmp':
            index += ins_type[1]
        
        try:
            repeat_check[index] += 1
        except:
            print('Instructions completed, acc = ' + str(acc))
            return True

    return False

def ins_permutations(original_instructions):
    
    test_ins = original_instructions
    
    for index, ins in enumerate(test_ins):
#        print(index, ins)
        if detect_instruction(ins)[0] == 'nop':
            test_ins[index] = 'jmp' + ins[3:]
            if run(test_ins) == True:
#                return test_ins
                return run(test_ins)
            else:
                test_ins[index] = 'nop' + ins[3:]

        if detect_instruction(ins)[0] == 'jmp':
            test_ins[index] = 'nop' + ins[3:]
            if run(test_ins) == True:
#                return test_ins
                return run(test_ins)
            else:
                test_ins[index] = 'jmp' + ins[3:]