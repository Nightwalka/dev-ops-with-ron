

import os


def check_file(folder):
    try:
        files = os.listdir(folder)
        return files,None
    except FileNotFoundError:
        return None, ("Please enter a valid file name")
    

def main():
    folder_paths = input("please enter the file names: ").split()
    for folder_path in folder_paths:

        files,error = check_file(folder_path)

        if files:
            print(f"{folder_path} has the following files")
            for file in files:
                print(file)
        else:
            print(f"{error}")


        

if __name__ =="__main__":
    main()
    