# Homework Assignment

# Problem 1

# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.


class Line:
    
  def __init__(self,coor1,coor2):
    self.x1, self.y1 = coor1
    self.x2, self.y2 = coor2
  
  def distance(self):
    dist = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2 )**(0.5)
    print(f"distance = {dist} unit")
  
  def slope(self):
    slp = (self.y2 - self.y1) / (self.x2 - self.x1)
    print(f"slope = {slp}")

coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())

# Problem 2
# Fill in the class

class Cylinder:
    
  def __init__(self,height=1,radius=1):
    self.height =  height
    self.radius = radius
      
  def volume(self):
    vol = 3.14 * (self.radius ** 2) * self.height
    print(f"volume of cylinder = {vol} cubic units") 
  
  def surface_area(self):
    sur = 2 * 3.14 * self.radius * (self.radius + self.height)
    print(f"surface area of cylinder = {sur} square unit")
    
  def __str__(self) -> str:
    print("Cylinder status")
  
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())