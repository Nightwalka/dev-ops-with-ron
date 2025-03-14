

def file_update(file_name,key,value):

    with open(file_name, "r") as file:
        lines = file.readlines()
    
    with open(file_name, "w") as file:

        for line in lines:

            if key in line:
                file.write(key + "=" +value+ "\n")

            else:
                file.write(line)

file_update("server.conf","MAX_CONNECTION","100101010")