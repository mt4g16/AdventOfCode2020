# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:18:17 2020

@author: Matteo
"""

my_file = open("input.txt", "r")
content = my_file.read()
instructions = content.split("\n")
my_file.close()

#print(instructions)

def gen_master(instructions):
    master = []
    for instruction in instructions:
        sub_ins = instruction.split(' contain ')
        ins_list = [sub_ins[0], sub_ins[1][:-1]]
        master.append(ins_list)
    return master

def check_parent(child_list):
    ins_list = gen_master(instructions)
    parents = []
#    print(ins_list)
    for child in child_list:
        #print(child)
        for rule in ins_list:
            if child in rule[1]:
                parents.append(rule[0])
    
    for child in parents:
        if child[:-1] == 's':
            child = child[:-1]
    new_parents = [sub[:-1] if sub[-1] == 's' else sub for sub in parents] 
    return new_parents
            

def exhaustive_check(input_origin):
    token = True
    origin = input_origin
    all_parents = []
#    print(origin)
    while token == True:
        if check_parent(origin):
            origin = check_parent(origin)
            all_parents.append(origin)
        if not check_parent(origin):
            token = False
#            print('Done')
            
    all_parents = [item for sublist in all_parents for item in sublist]
    all_parents = list(set(all_parents))
    print(len(all_parents))




#check_parent(['shiny gold bag'])
exhaustive_check(['shiny gold bag'])