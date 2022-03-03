list1 = [1,1,2,3]
list1.append(4)
print(list1)
print(list1.count(1))

x = [1, 2, 3]
x.append([4, 5])
print(x)

x = [1, 2, 3]
x.extend([4, 5])
print(x)

print(list1.index(2))
# if index position does not have any value then it returns ValueError

# Place a letter at the index 2
list1.insert(2,'inserted')
print(list1)

ele = list1.pop(1)  # pop the second element
print(ele)
print(list1)

list1.remove('inserted')
print(list1)

list1.remove(3)
print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

x = [1,2,3]
y = x.copy()
y.append(4)
print(y)
print(x)