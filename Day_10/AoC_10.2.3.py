# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 21:30:50 2020

@author: Matteo
"""
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

def perm2():
    
    lst = prep_sort(raw_adapters)
    device_adapter = max(lst) + 3
    
    lst_l = len(lst)
    
    cands_1 = []
    
#    test_vals = []
#    for t in int(lst_l/2):
#        test_vals.append([t])
    
    for p in range(1, 3):
        for k in range(lst_l):
            for j in range(lst_l):
                for index in range(lst_l):
                    index += k
                    temp = prep_sort(raw_adapters)
                    del temp[index:index+j:p]
                    print(temp)
                    temp.insert(0, 0)
                    temp.append(device_adapter)
                    if temp not in cands_1:
    #                    print(temp)
                        cands_1.append(temp)
                    
#    for m in range(lst_l):
        
    

    return(cands_1)

def iter_check(input_test_lsts):
    
#    for i in input_test_lsts:
#        print(i)
    viable = []
    
    for l in input_test_lsts:
        if check_viable(l) == True and (l not in viable):
            viable.append(l)
    
    print(viable, len(viable))
        

prep_sort(raw_adapters)


print(prep_sort(raw_adapters))
#print('-----------------------------------')



iter_check(perm2())








