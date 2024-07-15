# Meta caracteres: ^ $ \ ( )
# (1)  /1
# (1(2))  /1 /2
# (1(2))(3)  /1 /2 /3


import re

texto = '''
<p>Frase 1</p> <p>Segunda Frase</p> <p>Third one</p> <div>4</div>
'''

tags = re.findall(r'<([pdiv]{1,3})>(.+?)<\/\1>', texto)

# for tag in tags:
#     um, dois = tag
#     print(dois)


cpf = '123.456.789-10'
# print(re.findall(r'(?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2}', cpf))

# Rebuilding the tags

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1AAA\3BBB\4', texto))
