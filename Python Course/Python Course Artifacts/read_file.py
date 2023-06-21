try:
    with open('C:\\Users\\WillKraus\\Documents\\Personal Lists\\List_6_21.txt') as file:
        print (file.read())
        #NB: works only if in same folder if just listing document!
except FileNotFoundError:
    print("The file does not exist.")
