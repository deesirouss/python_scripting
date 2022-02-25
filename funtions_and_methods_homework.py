import string

# write a function that computes volume of a sphere given its radius

def vol(rad):
  # import math
  # return ((4/3) * math.pi * rad ** 3) , we can do this way too
  return ((4/3) * 3.14 * rad ** 3)

print(vol(2))

# write a funtion that checks whether a number is in given range(inclusive of high and low)

def ran_check(num, low, high):
  if num in range(low, high+1):
    return f"{num} is in the range {low} and {high}"
    #return (num in range(low, high + 1)) to return boolean value

print(ran_check(5,2,7))

# write a python fuction that accepts a string and calculates the number of upper case letters and lower case letters

def up_low(s):
  # d = {'upper': 0, 'lower': 0}, can be done this way too
  ups = 0
  lows = 0
  for char in s:
      if char.isupper():
        ups += 1
      elif char.islower():
        lows += 1
      else:
        pass
  print(f"ups = {ups}, lows = {lows}")
        
up_low('I am very Smart?')

# write a python function that takes a list and returns a new list wiht unique elements of the first list

def unique_list(lst):
  return list(set(lst))
  # can be done in his way too
  # seen_numbers = []
  # for number in lst:
    # if number not in seen_numbers:
      # seen_numbers.append(number)

print(unique_list([1,1,1,2, 4,2,3,3,3]))

# write a python funtion to multipy all the numbers in a list

def multiply(numbers):
  total = 1
  for num in numbers:
    total *= num
  return total
    

print(multiply([1,2,3, -4]))

# write a python function that check whether a word or phrase is palindrome or not

def palindrome(s):
  return s.replace(" ", "") == s[::-1].replace(" ", "")

print(palindrome('nurses run'))
print(palindrome('bibek'))
print(palindrome('helleh'))

# write a python function to check whether a string is pangram or not

def ispangram(str1, alphabet=string.ascii_lowercase):
  return set(alphabet) == set(str1.replace(" ", "").lower())
  # process defined in steps
  # alphaset = set(alphabet)
  # str_refactored = str1.replace(' ', '').lower()
  # strset = set(str_refactored)
  # return alphaset == strset
    
    

print(ispangram("The Quick brown fox jumps over the lazy dog"))