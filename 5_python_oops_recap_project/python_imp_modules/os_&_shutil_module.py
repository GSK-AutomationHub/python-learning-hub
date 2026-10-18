import os
import shutil

# to list file folder in location
print(os.getcwd())
print(os.listdir(os.getcwd()))

# to create file & write to it
f = open('practice.txt', 'w+')
f.write("this is the test string")
f.close()

# to move file from source to destination
filepath = "C:\\selenium_python_revision\\python_oops_revision_project\\python_adv_concepts"
#shutil.move('practice.txt',filepath)

# os.unlink(path) - to delete file , os.rmdir(path) - to delete empty folder
# shutil.rmtree(path) - to delete folder with content
# prefer pip install send2trash

for folder, sub_folder, files in os.walk(filepath):
    print(f"currently looking at folder {folder}")
    print(f"Sub_folders : {sub_folder}")
    print("Files:")
    for file in files:
        print(f"\t {file}")



