# Delete a file
import os
os.remove("demofile.txt")

# Check if file exists
"""To avoid getting an error, you might want to check if the file exists before you try to delete it"""
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# Delete folder
"""To delete an entire folder, use the os.rmdir() method"""
os.rmdir("myfolder")
