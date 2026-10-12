import operator
name_and_number = {'Derek':7,'Xavier':80,'Bob':612,'Chantanelle':9}
new_list = sorted(name_and_number.items(), key=operator.itemgetter(1), reverse=True)
for name,number in new_list:
    print(f"{name:16}: {number:8}")