# Validating an IPv4
import re


ip_reg_exp = re.compile(r'''
^
    (?:
        (?:
            25[0-5]| # de 250 a 255
            2[0-4][0-9]| # 200 a 250
            1[0-9]{2}| # 100 a 199
            [1-9][0-9]| # 10 a 99
            [0-9] # 10 a 99
        )\.
    ){3}
    (?:
        25[0-5]| # de 250 a 255
        2[0-4][0-9]| # 200 a 250
        1[0-9]{2}| # 100 a 199
        [1-9][0-9]| # 10 a 99
        [0-9] # 10 a 99
    )
    $
''', flags=re.X)

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'

    print(ip, ip_reg_exp.findall(ip))
