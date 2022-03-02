import os, shutil
f = open('practice.txt','w+')
f.write('This is a test string created by python open command')
f.close()
print(os.getcwd())
print(os.listdir('/home/bibek/git'))
os.remove('/home/bibek/git/python_scripting/Advance_python_modules/practice.txt')
shutil.move('practice.txt','/home/bibek/git/python_scripting/Advance_python_modules/')

print(os.listdir('/home/bibek/git/python_scripting/Advance_python_modules/'))

for folder, sub_folder, files in os.walk('/home/bibek/git/python_scripting/Advance_python_modules/'):
  print(f"Currenlty looking at {folder}")
  print(f"the sub-folders are: ")
  for sub in sub_folder:
    print(f"Subfolder: {sub}")
  print("the files are ")
  for f in files:
    print(f"file: {f}")
    