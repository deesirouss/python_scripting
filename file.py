from statistics import mode


myfile = open('myfile.txt')
print(myfile.read())
#after one read operation the cursoe goes to the end of the file, so we have to set it back to 0 position with seek(0) funtion 
myfile.seek(0)
contents = myfile.read()
myfile.seek(0)
print(myfile.readlines())
print(contents)
myfile.close()

with open('myfile.txt') as my_new_file:
  contents = my_new_file.read()
  print(contents)
  
with open('new_file', mode='w') as f:
  f.write('This is new file created by Python if it does not exits or it can overwrite this file if it already exist')

with open('new_file', mode= 'r') as r:
  print(r.read())

# Print hello using indexing
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# answer
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# answer
print(d['k1'][2]['k2'][1]['tough'][2][0])