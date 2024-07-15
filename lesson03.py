# Meta caracteres: ^ $ * + ? { } \ ( )
# * 0 ou n vezes
# + 1 ou n vezes
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais vezes
# {,10} de 0 a 10 vezes
# {5, 10} de 5 a 10 vezes
# {10} exatamente 10 vezes

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vemm!
'''

print(re.findall(r'Jo+ão+', texto, flags=re.I))
print(re.findall(r'Jo{1,}ão{1,}', texto, flags=re.I))
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))
# print(re.sub(r'jo+ão+', 'Felipe', texto, flags=re.I))

texto2 = 'João ama ser amado.'

print(re.findall(r'ama[do]*', texto2, flags=re.I))
