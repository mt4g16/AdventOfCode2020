# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 22:28:54 2020

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

def test_lst_gen(deviation):

    dev = deviation +1
    lst = prep_sort(raw_adapters)
    lst_len = len(lst)
    
    device_adapter = max(lst) + 3
    
    test_lsts = []
    
    test_lsts.append([0] + lst + [device_adapter])
    
    altern = 3
    
    for d in range(1, dev):
        
        for a in range(0, altern):
        
            for i in range(lst_len):
    #            print(prep_sort(raw_adapters))
                temp_check = prep_sort(raw_adapters)
    #            print('index:', i, ' dev:', d)
                
                forw_splice_strt = i+1
                forw_splice_end = i+d+1
                
                back_splice_strt = i-d
                
                if back_splice_strt < 0:
                    back_splice_strt = 0
                
                back_splice_end = i
                
                if a == 0 or a == 3:
                
    #            print(temp_check[forw_splice_strt:forw_splice_end], 'Forw')
                    del temp_check[forw_splice_strt:forw_splice_end]
    
                if a == 1 or a == 3:    
    #            print(temp_check[back_splice_strt:back_splice_end], 'Back')
                    del temp_check[back_splice_strt:back_splice_end]
                
    #            print(temp_check)
                temp_check.insert(0, 0)
                temp_check.append(device_adapter)
                test_lsts.append(temp_check)
    #            print()
    
    return test_lsts
    

def iter_check(input_test_lsts):
    
#    for i in input_test_lsts:
#        print(i)
    viable = []
    
    for l in input_test_lsts:
        if check_viable(l) == True and (l not in viable):
            viable.append(l)
    
    print(viable, len(viable))
        
    
    
adapters = prep_sort(raw_adapters)

#print(adapters)

for i in test_lst_gen(3):
    print(i)

#iter_check(test_lst_gen(3))


    
    
    
    
    
    
    