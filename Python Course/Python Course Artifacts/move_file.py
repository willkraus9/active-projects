import os
source = " "
destination = " "
    #move file from source to destination

try: 
    if os.path.exists(destination):
        print("There's a file already there")
    else:
        os.replace(source,destination)
        print(source+ " was moved.")
    
except FileNotFoundError:
    print(source+ " was not found.")