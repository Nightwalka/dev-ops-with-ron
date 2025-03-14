import os

def error_checker(folders):
    try:
        files = os.listdir(folders)
        return files,None
    except FileNotFoundError:
       
        return None, ("'"+folders+"does not exist")
    

def main():
    folder_paths = input("Please enter a valid folder separate name swith space:  ").split()
    for folder_path in folder_paths:

        files, error_message =error_checker(folder_path)

        if files:
            print(f"{folder_path} contains the following:")
            for file in files:
                print(file)
        else:
            print(f" Error in {folder_path}: {error_message}") 

if __name__ =="__main__":
    main()