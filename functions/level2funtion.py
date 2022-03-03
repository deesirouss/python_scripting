# level 2 Problem

# Find 33: given a list of ints, return True if the array contains a 3 next to a 3 somewhere

def find33(mylist):
  for i in range(len(mylist)-1):
    # if mylist[i:i+1] == [3,3] , we can do this way too
    if mylist[i] == mylist[i+1] == 3:
      return True  
  return False

print(find33([1,2,3]))
print(find33([1,3,3]))

# paper doll: Given a string, return a string for every character in the original there are three characters

def paper_doll(name):
  # resutl = ''
  # for char in name:
  #   resutl += char*3 , we can do this way too
  out = []
  for i in range(len(name)):
    v = name[i]*3
    out.append(v)
  return ''.join(out)

print(paper_doll("name"))

# blackJack : given three integers between 1 and 11, if their sum is less than 11 or equal to 21, return their sum. if their sum exceeds 21 and there's an eleven, reduce the total sum by 10. finally if the sum (even after adjustment) exceeds 21 return 'Bust'

def blackjack(a,b,c):
  if sum([a,b,c]) <= 21:
    return sum([a,b,c])
  elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
    return sum([a,b,c])-10
  else:
    return "Bust"
print(blackjack(1,11,5))  
print(blackjack(11,11,51))

# summer of 69: return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9(every 6 will be followed vy at least one 9), return 0 for no numbers

def summer69(arr):
  total = 0
  add = True
  for num in arr:
    while add:
      if num != 6:        
        total += num
        break
      else:
        add = False
    while not add:
      if num != 9:
        break
      else:
        add = True
        # break
  return total

print(summer69([1,2,3,]))
print(summer69([4,5,6,7,8,9]))
print(summer69([6,7,8,9]))