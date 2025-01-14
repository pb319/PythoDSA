import os

path = "write1.txt"
if os.path.exists(path):
    os.remove(path)
    print("File Deleted :)\n")
else:
    print("File Doesn't Exist ")