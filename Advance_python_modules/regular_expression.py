import re

text = "The person's phone number is 408-555-1234. Call soon!"
pattern = 'phone'
print(re.search(pattern,text))

# pattern = "Not in Text"
# print(re.search(pattern,text)) # returns none if do not find a match

match = re.search(pattern,text)
print(match)
print(match.span(), match.start(), match.end())

# But what if the pattern occurs more than once?
text = "my phone is a new phone"
match = re.search("phone",text)
print(match.span())

# If we wanted a list of all matches, we can use .findall() method:
matches = re.findall("phone",text)
print(matches, len(matches))

# we can iterate over it also using finditer
for match in re.finditer("phone",text):
  print(match.span(), match.group())


# Identifiers for Characters in Patterns
text = "My telephone number is 408-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone.group())

# Character	Description	Example Pattern Code	Exammple Match
# \d	A digit	file_\d\d	file_25
# \w	Alphanumeric	\w-\w\w\w	A-b_1
# \s	White space	a\sb\sc	a b c
# \D	A non digit	\D\D\D	ABC
# \W	Non-alphanumeric	\W\W\W\W\W	*-+=)
# \S	Non-whitespace	\S\S\S\S	Yoyo

phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phone.group())

# groups
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
print(results.group())
print(results.group(1))
print(results.group(3))

# Character	Description	Example Pattern Code	Exammple Match
# +	Occurs one or more times	Version \w-\w+	Version A-b1_1
# {3}	Occurs exactly 3 times	\D{3}	abc
# {2,4}	Occurs 2 to 4 times	\d{2,4}	123
# {3,}	Occurs 3 or more	\w{3,}	anycharacters
# \*	Occurs zero or more times	A\*B\*C*	AAACC
# ?	Once or none	plurals?	plural

# Additional Regex Syntax

# or operator
print(re.search(r"man|woman","This man was here."))
print(re.search(r"man|woman","This woman was here."))

# The Wildcard Character
print(re.findall(r".at","The cat in the hat sat here."))
print(re.findall(r".at","The bat went splat"))
print(re.findall(r"...at","The bat went splat"))
print(re.findall(r'\S+at',"The bat went splat"))

# Starts with and Ends With

# Ends with a number
print(re.findall(r'\d$','This ends with a number 2'))

# Starts with a number
print(re.findall(r'^\d','1 is the loneliest number.'))

# Exclusion
phrase = "there are 3 numbers 34 inside 5 this sentence."
print(re.findall(r'[^\d]',phrase))
# To get the words back together, use a + sign
print(re.findall(r'[^\d]+',phrase))

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
clean = ' '.join(re.findall('[^!.? ]+',test_phrase))
print(clean)

# Brackets for Grouping
text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
print(re.findall(r'[\w]+-[\w]+',text))

# Parenthesis for Multiple Options

# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"
print(re.search(r'cat(fish|nap|claw)',text))
print(re.search(r'cat(fish|nap|claw)',texttwo))
# None returned
print(re.search(r'cat(fish|nap|claw)',textthree))