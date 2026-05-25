####2.3-Criando e maniupulando texto: strings

#coding: utf-8
"""copa 2014"""

print('copa do mundo 2014'

'''2014 - Copa do mundo
'''

" copa 'padrão fifa'"

'copa "padrão fifa"')

print("""
Uso: consulta_base [OPCOES]
     -h       Exibe saida de ajuda
     -U url   Url do dataset
""")

print(("Copa" "2014") == "Copa2014")

input('Em qual cidade o legado da copa foi relevando '
      'para a população: ')

####len(strings), explicação len e para o tamanho da string

st = "maracana"

print(st[0])

print(st[1:4])

print(st[2:])

print(st[:3])

print(len(st))


####Sequencias string

print("m" in "macarana")

print("x" not in "macarana")

print("m" +"aracana")

print("a" * 3)


####imutabilidade: novas strings criadas a partir de outras strings

minha_str = "livro python 3"
print(minha_str[13] + "2")

# (minha_str[13] = "2")
# File "/Users/rlresende/python_escreva_seu_primeiro_pragrama/pythonProject1/Capitulo 2 : aprendendo python na pratica número e strings/2.3-Criando e maniupulando texto: strings.py", line 59
#     (minha_str[13] = "2")
#                    ^
# SyntaxError: invalid syntax

print('\n')

####copiando e manipulando texto com a string

minha_str1 = "livro python 3"
minha_str1 = minha_str1[0:13] + "2"
print(minha_str1)

minha_str2 = "livro python 3"
minha_str2 = minha_str2.replace("3","2")
print(minha_str2)

print("macarana".capitalize())

print("macarana".count("a"))

print("macarana".startswith("m"))

print("macarana".endswith("z"))

print("copa de 2014".split(" "))

print(" ".join(["Copa","de" ,"2014"]))

print("copa de 2014".replace("2014","2018"))


####interpolando a string
print(("%d dias para copa") % (100))

print("{} dias para copa".format(100))

print("{dia} dias para copa".format(dia=100))

print("{:<<60}".format("alinhados á esquerda, ocupando 60 posições"))

print("{:>>60}".format("alinhados á esquerda, ocupando 60 posições"))

print("{:^^60}".format("centralizados á esquerda, ocupando 60"))


####operações misturados tipos diferentes e as regras de coerção

print(100 * 1.3) #preço mais de 30%
print(100 * 1.4)
print(100 * 1.5)
print(100 * 1.6)

####explorando as operações por conta propria

print(type(1 + 2.0))

print(type(1 + 2j))

print(type(1.0 + 1.0 + 1.2 + 9.9))