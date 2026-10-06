from operator import itemgetter

data = [['Derek',7],['Xavier',80],['Bob',612],['Chantanelle',9]]
data.sort(key=itemgetter(1),reverse=True)

for row in data:
    print(f"{row[0]:16} : {row[1]:8}")