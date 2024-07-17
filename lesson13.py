import re
from pprint import pprint

strong_password_regex = re.compile(
    r'^'
    r'(?=.*[A-Z])'
    r'(?=.*[a-z])'
    r'(?=.*[0-9])'
    r'(?=.*[-\/:-@[-`{-~])'
    r'.{12,}'
    r'$',
    flags=re.M
)

test_str = ("VÁLIDAS\n"
            "y|3f4S{7KW{o\n"
            "HwxCmD8.6;0?\n"
            "{4r4Zw/tGX0{\n"
            "jgU?0W9~#Z6p\n"
            "G2&t]TZ2}r5c\n\n"
            "SEM MINÚSCULAS\n"
            "8:\\0?K1SP7_L\n"
            "973*<HBU5;C<\n"
            "\\KG]G|Z6902\"\n"
            ".WE-248\\}K9Q\n"
            "1$F3L4NK:{\\3\n\n"
            "SEM MINÚSCULAS E NÚMEROS\n"
            "CVXN>^:^\\IV~\n"
            "*J~\"PWJAG=:`\n"
            "F%>}~MTW{{BI\n"
            "M@BIML!\"R#{[\n"
            "~$M[E~L?N'LZ\n\n"
            "SEM NÚMEROS CARACTERES E MINÚSCULAS\n"
            "DZIOPMRXJZSA\n"
            "UZBFITPWSXCZ\n"
            "UTGQTOGNEHVM\n"
            "LMLTVFAJKNRT\n"
            "JOOEHEVOOFAY\n\n"
            "QUANTIDADE INVÁLIDA (6)\n"
            "Et5^4s\n"
            "04z[Qi\n"
            "h;Fr83\n"
            "4C0lo'\n"
            "iFf:64")

pprint(strong_password_regex.findall(test_str))
