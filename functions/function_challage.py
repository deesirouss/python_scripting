# Challange Problems 

# spy_game: write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
  # definning list of 007
  code = [0,0,7]
  
  for num in nums:
    if num == code[0]:
      code.pop(0)
    
  return len(code) == 0

print(spy_game([1,2,3,4,5]))
print(spy_game([0,0,12,35,7]))

# count primes: write a function that returns the number of prime numbers that exist up to and including a given number
# by convention we'll treat 0 and 1 as not prime

def count_primes(num):
  if num < 2:
    return 0
  # prime number list
  primes = [2]
  # counter
  x = 3
  while x <= num:
    # for y in primes: we can do this way too
    for y in range(3,x,2):
      if x % y == 0:
        x += 2
        break
      
    else:
      primes.append(x)
      x += 2
  print(primes)
  return len(primes)

print(count_primes(100))