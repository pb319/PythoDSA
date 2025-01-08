# Let say - we want to write a file
path_write = "write.txt"
with open(path_write, mode= "w") as file:
    file.write("This is the first line\n")
    file.writelines(["I love meditation!\n", "I love Coding"])
