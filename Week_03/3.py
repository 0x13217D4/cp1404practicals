names = ["Bob", "John", "Michael", "David"]
times = 0
for name in names:
    times += 1
    with open(name + ".txt", "a") as out_file:
        print(times, file=out_file)