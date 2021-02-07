# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 19:57:26 2020

@author: Matteo
"""
import itertools

my_file = open("input.txt", "r")
content = my_file.read()
raw_adapters = content.split("\n")
my_file.close()


def prep_sort(lst):
    lst = [int(x) for x in lst]    
    lst.sort()
    return lst

def check_viable(lst):
    diff = []
    for index_a in range(1, len(lst)):
        diff.append(lst[index_a]-lst[index_a-1])
    
    for i in diff:
        if i > 3:
            return False
    
    return True

def permutations(lst):
    working_lst = lst
        
    all_combinations = []
    
    device_adapter = max(lst) + 3
    
    viable_comb = []
    
    for r in range(len(working_lst) + 1):        
        combinations_object = itertools.combinations(working_lst, r)
        combinations_list = list(combinations_object)
        combinations_list = [list(elem) for elem in combinations_list]

#        print(combinations_list)
        
        for i in combinations_list:
            if type(i) == list:
                temp_1 = [0]
                for q in i:
                    temp_1.append(q)

                temp_1.append(device_adapter)
                all_combinations.append(temp_1)
#    print(all_combinations)
    
    for comb in all_combinations:
#        print(comb)
        if check_viable(comb) == True:
            viable_comb.append(comb)
#            print(True)
#        else:
#            print(False)
    
    print(len(viable_comb))


#test = [0, 1, 4, 5, 6, 7, 10, 11, 12, 16, 19, 22]

adapters = prep_sort(raw_adapters)
permutations(adapters)
