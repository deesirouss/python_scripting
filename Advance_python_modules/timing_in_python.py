import time

def func_one(n):
  '''
  Given a number n, returns a list of string integers
  ['0','1','2',...'n]
  '''
  return [str(num) for num in range(n)]

def func_two(n):
  '''
  Given a number n, returns a list of string integers
  ['0','1','2',...'n]
  '''
  return list(map(str,range(n)))

# time consumed by the first function
start_time = time.time()
result = func_one(1000000)
elapsed_time = time.time() - start_time
print(elapsed_time)

# time consumed by the second function
start_time = time.time()
result = func_two(1000000)
elapsed_time = time.time() - start_time
print(elapsed_time)

# Timeit Module
import timeit
# timeit requires setup, stmt and number of time to execute the function

# setup for first function
setup = '''
def func_one(n):
  return [str(num) for num in range(n)]
'''

stmt = 'func_one(100)'

elapsed_time = timeit.timeit(stmt,setup,number=100000)
print(elapsed_time)

#setup for second function
setup2 = '''
def func_two(n):
  return list(map(str,range(n)))
'''
stmt2 = 'func_two(100)'
elapsed_time = timeit.timeit(stmt2,setup2,number=100000)
print(elapsed_time)

# we can distinguish the time more efficiently if we increase the number of time timeit execute the function