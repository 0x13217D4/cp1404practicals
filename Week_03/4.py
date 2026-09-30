with open("test.txt","r") as out_file:
    for line in out_file:
        name = line.split()[0]
        years = line.split()[2]
