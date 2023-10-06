import os
import shutil

path = 'test2.txt'
# path = "empty_folder"
# path = "folder"

try:
    os.remove(path)        # delete a file
    # os.rmdir(path)       # delete a file or empty folder
    # shutil.rmtree(path)  # delete files and folders
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:
    print("You do not have permission to delete that.")
except OSError:
    print("You cannot delete that using that function.")
else:
    print(path + "was deleted.")
