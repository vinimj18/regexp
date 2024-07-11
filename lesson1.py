import re

# search, findall, sub

string = 'Essa é uma string teste de expresões teste regulares'

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'Firenze', string))

regexp = re.compile(r'teste')

print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('Firenze', string))
