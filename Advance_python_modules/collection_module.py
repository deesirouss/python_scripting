from collections import Counter, defaultdict, namedtuple

mylist = [1,1,1,1,2,2,2,3,3,3,4,4,4,4]
print(Counter(mylist))

list2 = ["a","a","a",10,10,10,9]
print(Counter(list2))
print(Counter('aaabbbccdddeeffggggtt'))

sentence = "how many times does each word show up in this list with a word"
print(Counter(sentence.split()))
c = Counter('aaabbbccdddeeffggggtt')
print(list(c))

d = defaultdict(lambda: 0)
d['value'] = 100
print(d['wrong key'])
print(d)

dog = namedtuple('Dog',['age','breed','name'])
sammy = dog(age=5,breed='Husky', name='Sam')
print(sammy)
print(sammy.name)
print(sammy[1])