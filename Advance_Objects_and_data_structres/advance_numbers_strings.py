# Hexadecimal & Binary
print(hex(246), hex(512), bin(1234), bin(128), bin(512))

# Exponentials
print(pow(3,4), pow(3,4,5)) # i.e. (3 ^^ 4) % 5

# Absolte and Round
print(abs(-3.14), abs(3), round(3,3), round(395,-2), round(3.1415926535,2))

# strings
s = 'hello world'
print(s.capitalize(), s.upper(), s.lower(), s.count('o'), s.find('o'), s.center(20,'z'), 'hello\thi'.expandtabs())

# is check methods

s = 'hello'

print(s.isalnum(), s.isalpha(), s.islower(), s.isspace(), s.istitle(), s.isupper(), s.endswith('o'))

# built in regular expression

print(s.split('e'), s.partition('l'))