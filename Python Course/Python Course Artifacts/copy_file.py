import shutil

#copyfile() = copy contents
#copy() = copyfile + permission + destination can be a directory
#copy2() = copy() + metadata (creation + modification times)

shutil.copyfile('test.txt','copy.txt') #copy.txt can be replaced with the file path
