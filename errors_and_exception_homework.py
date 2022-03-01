# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.

# for i in ['a','b','c']:
#     print(i**2)

for i in ['a','b','c']:
  try:
    print(i**2)
  except TypeError:
    print(f"whoops {i} is not a number")
  
# Problem 2
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

# x = 5
# y = 0

# z = x/y
x = 5
y = 0
try:
  z = x/y
except ZeroDivisionError:
  print(f"you cannot divide anything by {y}")
finally:
  print("All Done.")
  
# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
  while True:
    try:
      number = int(input("Enter a number to get square of it "))
    except:
      # print(f"sorry {number} is not a number")
      print("Gonna ask u again")
      # continue
    else:
      sqr = number ** 2
      print(f"squrae of the {number} is {sqr}")
      break
      
ask()