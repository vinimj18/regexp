"""
\w -> [0-9a-zA-ZÀ-ú_]
\w -> [0-9a-zA-Z_] -> re.A
\W -> [^0-9a-zA-ZÀ-ú_]
\W -> [^0-9a-zA-Z_] -> re.A
\d -> [0-9]
\D -> [^0-9]
\s -> [ \r\n\f\v\t]
\S -> [^ \r\n\f\v\t]
\b -> border
\B -> not border

"""

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# print(re.findall(r'[0-9a-zA-ZÀ-ú_]+', texto))
# print(re.findall(r'\w+', texto))
# print(re.findall(r'\w+', texto, flags=re.A))
# print(re.findall(r'\W+', texto))
# print(re.findall(r'\W+', texto, flags=re.A))
# print(re.findall(r'\d+', texto))
# print(re.findall(r'\D+', texto))
# print(re.findall(r'\s+', texto))
# print(re.findall(r'\S+', texto))
# print(re.findall(r'\S+', texto))
# print(re.findall(r'\be\w+', texto))
# print(re.findall(r'\w+e\b', texto))
# print(re.findall(r'\b\w{4}\b', texto))  # pegas as palavras com 4 caracteres
# print(re.findall(r'\w{4}', texto))  # corta as palavras
print(re.findall(r'flo\B', texto))
print(re.findall(r'flores\B', texto))
