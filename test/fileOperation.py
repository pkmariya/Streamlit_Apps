
import os

try:
    myFile = open("mariya preeths.txt", 'a+')
    myFile.write("File name is: ")
    myFile.write(myFile.name)
    myFile.write("\nFile mode is: ")
    myFile.write(myFile.mode)
    myFile.write("\n Current working directory is")
    myFile.write(os.getcwd())
except IOError, e:
    print("Can't find the file or write data", e)
else:
    print("Sucessfully written into file")
    print("file location is: ", os.getcwd() + "/" + myFile.name)
    myFile.close()

