
import os

folders = input("Please enter the folder names with spaces between : ").split()

for folder in folders:
    
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Folder name is incorrect, please enter a valid name ",folder) 
        continue
    except PermissionError:
        print("Seems like you dont have access to the folder",folder)        
    
    print("list of files in the folder "+folder)
    for file in files:
        print(file)
            