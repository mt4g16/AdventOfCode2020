# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 22:54:21 2020

@author: Matteo
"""
import numpy as np

my_file = open("input.txt", "r")
content = my_file.read()
instructions = content.split("\n")
my_file.close()

#print(instructions)

def gen_master(instructions):
    master_dic = {}
    for instruction in instructions:
        sub_ins = instruction.split(' contain ')
#        print(contents_org(sub_ins[1][:-1]))
        
        master_dic[singularize(sub_ins[0])] = contents_org(sub_ins[1][:-1])
    return master_dic


def singularize(string):
    if string[-2:] == 's,':
        return string[:-2]
    
    if string[-1] == 's':
        return string[:-1]
    
    if string[-1] == ',':
        return string[:-1]
    

        
    else:
        return string

def contents_org(raw_string):
    raw_string_lst = raw_string.split(' ')
    
    div = len(raw_string_lst)/4

    if raw_string_lst[0] != 'no':
        temp_cont = []
        sub_content = (np.array_split(raw_string_lst, div))
        for x in sub_content:
            temp_0 = []
            temp_0.append(int(x[0]))
            temp_1 = (x[1:len(x)].tolist())
            temp_2 = ' '.join(temp_1)
            temp_0.append(singularize(temp_2))
            temp_cont.append(temp_0)

        return temp_cont
    else:
        return None
        

def get_child(bag_name_lst):
    return ins_dic.get(bag_name_lst[1])

def exhaustive_child(input_quant, input_name):
    
    origin = [input_quant, input_name]
    
    master_nest = []
    master_nest.append(origin)

    
    for quant_bag in master_nest:
        if type(quant_bag) != int:
            child = get_child([quant_bag[0], quant_bag[1]])
#            print(child)
            if child != None:
#                master_nest.append(len(child))
                for quant_bag in child:
#                    print(quant_bag[0])
                    for quant in range(quant_bag[0]):
                        master_nest.append([1, quant_bag[1]])
                

    return master_nest



def flatten_toint(l):
    x = []
    for i in l:
        if type(i) is list:
            x.extend(i)
        else:
            x.append(i)
        
    y = [j for j in x if not isinstance(j, str)]
        
    return y



ins_dic = gen_master(instructions)

final = exhaustive_child(1, 'shiny gold bag')

print(len(final)-1)