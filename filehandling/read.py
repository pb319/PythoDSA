

path_read = "read.txt"
with open(file=path_read,mode="r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)

