import re

# r is raw string
# escape the escape
pattern = re.compile(r'([a-zA-Z]).([a])')
string = 'search this inside of this text please'

print('search' in string)

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a.span(), a.start(), a.end(), a.group())

print(a,b,c,d)

