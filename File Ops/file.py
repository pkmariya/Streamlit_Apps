
try:
    f = open("message.txt", "r")
    content = f.read()
    print("Content of Message.txt is: \n", content)

    f = open("python.txt", 'w')
    f.write("Python is awesome!")
    
    f = open("python.txt", "r")
    new_content = f.read()
    print("Newly added content is: \n", new_content)

except:
    print("Please check the file name & location")

finally:
    f.close()

# *** Another way of achieving the same result *** 

# with open("message.txt", 'r') as f:
#     content = f.read()
#     print(content)

