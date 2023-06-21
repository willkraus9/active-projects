import os 
#get TODO list from computer
path = "C:\\Users\\WillKraus\\Documents\\Personal Lists\\List_6_21.txt"
if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file.")
else:
    print("That location does not exist.")


