# Meta caracteres: ^ $ * + ? { } \ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1

import re

texto = '<p>Frase 1</p> <p>Segunda Frase</p> <p>Third one</p> <div></div>'

# GREEDY: Vai até o final procurando um fechamento
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))

# NON GREEDY (LAZY): Retorna o valor assim que encontra um fechamento
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))
