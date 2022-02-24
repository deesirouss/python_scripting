# warmup Problems
# Lesser of two evens: Write a function that returns the lesser of teo given numbers if both numbers are even, but returns the greater if one or both numbers are odd
from ntpath import join
from tabnanny import check


def myfunc(a,b):
  if a % 2 == 0 and b % 2 == 0:
    if a != b:
      return min(a,b)
    else:
      return f"equal numbers: {a} {b}"
  else:
    if a != b:
      return max(a,b)
    else:
      return f"equal numbers: {a} {b}"

print(myfunc(8,9))
print(myfunc(4,8))

# Animal Crackers: Write a funtion that takes two-word string and returns True if both words begin with same letter

def animal_cracker(word):
  check = word.lower().split()
  # return check[0][0] == check[1][0]
  if check[0][0] == check[1][0]:
    return True
  else:
    return False
  
print(animal_cracker('Level level'))
print(animal_cracker('not level'))

# makes twenty: given teo integers, return True if the sum of the integers is 20 or if one of the integers is 20. if not return false

def makes_twenty(a,b):
  # return a == 20 or b == 20 or (a+b) == 20
  if a == 20 or b == 20 or (a+b) == 20:
    return True
  else:
    return False

print(makes_twenty(2,3))
print(makes_twenty(20,4))
print(makes_twenty(10,10))

# Level 1 Problem

# old_macdonald: write a funtion that capitalizes the first and fourth letters of name

def old_macdonald(name):
  # first_half = name[:3]
  # second_half = name[3:]
  # return first_half.capitalize() + second_half.capitalize()
  out = []
  for w in range(len(name)):
    if w == 0 or w == 3:
      out.append(name[w].upper())
    else: 
      out.append(name[w])
  return ''.join(out)

print(old_macdonald('bibek'))

# Master yoda: given a sentence, return a sentence with the words reversed
def master_yoda(sentence):
  my_list = reversed(sentence.split())
  return ' '.join(my_list)

print(master_yoda('My name is'))