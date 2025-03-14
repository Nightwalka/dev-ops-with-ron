import os

folders = input(" Enter the folders separated by space:  ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError :
        print( "'"+folder+"' does not exist")
        break
    print("The folder "+folder+ "contains --->")
    for file in files:
        
        print(file)









































# import os 

# folders = input("Please provide the list of folders names with spaces in betwee: ").split()

# for folder in folders:
#     try:
#         files = os.listdir(folder)
#     except FileNotFoundError:
#         print("Please input correct folder '"+folder+"'  does not exist")
#         break
    
#     print("listing files to ---> "+ folder)
#     for file in files:
#         print(file)