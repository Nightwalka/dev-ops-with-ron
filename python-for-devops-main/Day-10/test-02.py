

import os 

def error_checker(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        
        return None,folder+" is not in the system"

def main():
    folders=input("pelase enter the folder name:  ").split()
    for folder in folders:
        files, error_message = error_checker(folder)
        if files:
            print(f"{folder} contians:")
            for file in files:
                print(file)
        else:
            print(f'{error_message}')
            


if __name__=="__main__":
    main()
    