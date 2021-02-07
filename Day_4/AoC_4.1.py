# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 22:42:34 2020

@author: Matteo
"""

my_file = open("input.txt", "r")
content = my_file.read()
raw_ids = content.split("\n\n")
my_file.close()

#print(raw_ids)

#valid_count = 0

def check_cat_num():
    cat_valid = []
    for raw_id in raw_ids:
        id_cat_list = []
        proc_1 = raw_id.split('\n')
        for cat in proc_1:
            id_cat_list.append(cat.split(" "))
        id_cat_list = sum(id_cat_list, [])
        #print(id_cat_list)
        
        id_dic = {}
        
        for cat in id_cat_list:
            anchor = cat.find(':')
            id_dic[cat[:anchor]] = cat[anchor+1:]

        
        cat_check = ('eyr', 'hcl', 'hgt', 'byr', 'iyr', 'pid', 'ecl')
        if all (cat in id_dic for cat in cat_check):
            #valid_count += 1
            cat_valid.append(id_dic)
    #print(cat_valid)
    return cat_valid
            
a = check_cat_num()
#print(len(a))
#print(valid_count)

def validate(id_dic):
    count = 0
    for id_data in id_dic:
        check = 0
        if (2020 <= int(id_data.get('eyr')) <= 2030) and (len(id_data.get('eyr')) == 4):
            check += 1
        if (2010 <= int(id_data.get('iyr')) <= 2020) and (len(id_data.get('iyr')) == 4):
            check += 1
        if (1920 <= int(id_data.get('byr')) <= 2002) and (len(id_data.get('byr')) == 4):
            check += 1
        
        if (id_data.get('hgt')[-2:] == 'cm') and (150 <= int(id_data.get('hgt')[:-2]) <=193):
            check +=1
        
        
        if (id_data.get('hgt')[-2:] == 'in') and (59 <= int(id_data.get('hgt')[:-2]) <=76):
            check +=1
        
        
        ok = '0123456789abcdef'
        if (id_data.get('hcl')[0] == '#' and all(c in ok for c in id_data.get('hcl')[1:]) and len(id_data.get('hcl')[1:]) == 6):
            check += 1
        
        ecl_check = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
        if id_data.get('ecl') in ecl_check:
            check += 1
        
        pid_check = '0123456789'
        if (len(id_data.get('pid')) == 9) and any(c in pid_check for c in id_data.get('pid')):
            check += 1
        
        #print(check)
        
        if check == 7:
            count += 1
            #print(id_data)
        
    return count

print(validate(a))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    