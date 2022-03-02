import math
#print(help(math))

value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(value))

print(math.pi)
# we can also import pi from math and use it
from math import pi
print(pi)

print(math.e, math.tau, math.inf, math.nan)

print(math.log(math.e), math.log(10), )

# custom base of log
# math.log(x,base)

print(math.log(100,10))

# trigonometric Functions

# Radians
print(math.sin(10), math.degrees(pi/2), math.radians(180))

# Random Module

import random
# these two line willproduce new numbers everytime
print(random.randint(0,100))
print(random.randint(0,100))

# random.seed(101) # scince this is declared all the random values will be same each time we execute this file
# but when we declare seed, these three randint will choose same number everytime
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))

# grabbing a random item from a list
mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))

# sample with replacement
print(random.choices(population=mylist,k=10))

# sample without replacement
print(random.sample(population=mylist,k=10))

# uniform distribution
print(random.uniform(a=0,b=100))

# normal/gaussian distribution
print(random.gauss(mu=0,sigma=1))