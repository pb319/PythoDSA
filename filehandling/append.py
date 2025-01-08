# In case of writing new lines without overwriting
append_path = "write.txt"
with open(append_path, mode="a") as file:
    file.write("\nThis is the END!")
