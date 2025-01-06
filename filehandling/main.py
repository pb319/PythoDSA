

path = "write.txt"
with open(file=path,mode="r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)