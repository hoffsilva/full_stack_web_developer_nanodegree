import os
directory = "/Users/hoffhenrypereiradasilva/Google Drive/Nanodegree Full Stack Web Developer/full_stack_web_developer_nanodegree/Lesson4/prank"
listFiles = os.listdir(directory)
print(listFiles)
print(os.getcwd())
os.chdir(directory)
print(os.getcwd())

for file in listFiles: 
    newName = file.translate(None, "0123456789")
    print("Old name: " + file)
    print("New name: " + newName)
    os.rename(file, newName)

os.chdir("/Users/hoffhenrypereiradasilva/Google Drive/Nanodegree Full Stack Web Developer/full_stack_web_developer_nanodegree/Lesson4")

