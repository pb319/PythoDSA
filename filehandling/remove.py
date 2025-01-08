import os

path = "write.txt"
if os.path.exists(path):
    os.remove(path)
    print("File Deleted :)\n")
else:
    print("File Doesn't Exist :(")