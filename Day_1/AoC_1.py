my_file = open("input.txt", "r")
content = my_file.read()
expense_report = content.split("\n")
my_file.close()
#print(expense_report)

check = False

for index, value in enumerate(expense_report):
    if check == False:
        for index2, value2 in enumerate(expense_report):
            if index != index2:
                if int(value)+int(value2) == 2020:
                    print(int(value)*int(value2))
                    check = True
                