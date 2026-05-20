# Capitulo 1: Iniciando com python

print(1)

a = int(input("Digite um numero (a): "))
b = int(input("Digite um numero (b): "))
c = int(input("Digite um numero (c): "))

for i in range(int(a),int(b),int(c)):
    print(int(a + b + c) * i)

print("Hello World")

# Capitulo 2: aprendendo python na prática números e strings

2.1-numeros

print(1) #int

print(1.0) #float

print(1.) #float tambem

print(1+2j) #complex

Gerando numeros por meios das funções embutidos

int(1.0)

int('9')

float(1)

float('9.2')

float('-inf')

float('+inf')

float('nan')

complex(1,2)

ints e longs unificando no python 3

Alguns exemplos de números e manipulações simples

print(3 + 2)

print(3 + 4.2)

print(4/2)

print(5/2)

print(5//2)

print(complex(1,2) + 2)

print(complex(2,0) + 0 + 1j)

print(2 + 0 + 1j)

operadores aritmeticas

print(1 + 2)

print(3 - 1)

print(10/2)

print(10//3)

print(10 * 2 + 1)

print(10 % 3)

print(-3)

print(2 ** 8)

operadores de bits

print(1|0)

print(1 | 5)

print(1^5)

print(4 & 1)

print(1 << 2)

print(4 >> 2)

print(~4)

operações misturando tipos diferentes e as regras de coerção

print(100* 1.3) #preço mais 30%

type(1 + 2.0)

type(1+2j)

type(1.0+2j)

type(1.0+1.0)

2.3-Criando e maniupulando texto: strings

#coding: utf-8
"copa 2014"


'copa do mundo 2014'

'''2014 - Copa do mundo
'''

" copa 'padrão fifa'"

'copa "padrão fifa"'

print("""
Uso: consulta_base [OPCOES]
     -h       Exibe saida de ajuda
     -U url   Url do dataset
""")

print(("Copa" "2014") == "Copa2014")

input('Em qual cidade o legado da copa foi relevant'
      'para a população')

len(strings), explicação len e para o tamanho da string

st = "macarana"

st[0]

st[1:4]

st[2:]

st[:3]

len(st)

Sequencias string

print("m" in "macarana")

print("x" not in "macarana")

("m" +"aracana")

"a" * 3

imutabilidade: novas strings criadas a partir de outras strings

minha_str = "livro python 3"
print(minha_str[13] + "2")

copiando e manipulando texto com a string

minha_str = "livro python 3"
minha_str = minha_str[0:13] + "2"
print(minha_str)

minha_str = "livro python 3"
minha_str = minha_str.replace("3","2")
print(minha_str)

"macarana".capitalize()

"macarana".count("a")

"macarana".startswith("m")

"macarana".endswith("z")

"copa de 2014".split(" ")

" ".join(["Copa","de" ,"2014"])

"copa de 2014".replace("2014","2018")

interpolando a string

(("%d dias para copa") % (100))

"{} dias para copa".format(100)

"{dia} dias para copa".format(dia=100)

"{:<60}".format("alinhados á esquerda, ocupando 60 posições")

"{:>60}".format("alinhados á esquerda, ocupando 60 posições")

"{:^60}".format("centralizados á esquerda, ocupando 60")

operações misturados tipos diferentes e as regras de coerção

print(100 * 1.3) #preço mais de 30%

explorando as operações por conta propria

type(1 + 2.0)

type(1 + 2j)

type(1.0 + 1.0)

Capitulo 3: Manipulações básicas

#Capitulo 3:Manipulações básicas

####3.1 Uma calculadora: o exemplo revisado

imposto = 0.27

salario = 5000

print("Salario real: {}".format(salario - (salario * imposto)))

print("Imposto: {}".format(salario * imposto))

####Aplicando formatação da strings é um float

imposto = 0.27

salario = 3000

print("Valor real: {0}".format(salario - (salario * imposto)))

####3.2-Pegando dados no terminal

salario = int(input("Digite o salário: "))

imposto = float(input("Imposto em % (exemplo: 27.5)? "))

print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

####3.3-Comparações: maior, menor, igual e outras

print(1 >= 1)

print(2 < 1)

print(9 == 9)

print(9 != 8)

print(2 <= 3)

print(1 == 1.0)

# print(10 >1j)
# TypeError: '>' not supported between instances of 'int' and 'complex'

####3.4-Condicionais if else elif e else

salario = int(input("Salario? "))

imposto = float(input("Imposto? "))

if imposto == '':
  imposto = 27.5
else:
  imposto = float(imposto)

print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

####indentação dos blocos de códigos

imposto = float(input("Imposto? "))

if imposto < 10:
  print("Medio")
elif imposto < 27.5:
  print("Alto")
else:
  print("Muito alto")

####Expressão if

imposto = 0.3

"alto" if imposto > 0.27 else "baixo"


imposto = 0.10

"alto" if imposto > 0.27 else "baixo"

valor_imposto = "alto" if imposto > 0.27 else "baixo"

print(valor_imposto)

####3.5 Operações logicos

imposto = float(input("Imposto? "))

if imposto < 10:
  print("baixo")
elif imposto >= 10. and imposto <= 27.:
  print("medio")
elif imposto > 27. and imposto < 100:
  print("alto")
else:
  print("imposto invalido")


####3.6 - loops com while

salario = float(input("Salario? "))

imposto = 27.

while imposto > 0:
  imposto = (input("Imposto ou (0) para sair: "))
  if not imposto:
    imposto = 27.
  else:
    imposto = float(imposto)
  print("Valor real: {0} ".format(salario - (salario * (imposto * 0.01))))

####o loop pode ser interrompido com um comando break

salario = int(input("Salario? "))

imposto = 27

while imposto > 0:
  imposto = input("Imposto ou (s) para sair: ")
  if not imposto:
    imposto = 27.
  elif imposto == 's':
    break
  else:
    imposto = float(imposto)
  print("Valor real: {0} ".format(salario - (salario * (imposto * 0.01))))


####3.7 - primeiro estrutura de dados: listas

lista = [1,2,3,4,5]
print(lista)

lista = ["salario","imposto"]
print(lista)

lista = [1, "salario"]
print(lista)

lista = [[1,2,3], "salario",10]
print(lista)

####Sequencia de lista em python ou seja podemos perguntar seu tamanho e acessar elementos por indices ou trechos

lista =["impostos","salario","altos","baixos"]

lista[0]

lista[-1]

lista[2:4]

####lista são mutaveis

lista = ["impostos","salarios","altos","baixos"]

lista[2] = "altos"

lista[3] = "baixo"

print(lista)

####ifs e listas

lista = []

if lista:
  print("Nunca sou executado")
else:
  print("Sempre sou executado")

####3.8 loop pythônicos com for e listas

imposto = ['MEI','Simples']

for imposto in imposto:
  print(imposto)

####comando for em detalhe

lista = [0,1,2,3,4,5,6,7,8,9,10]

for i in lista:
  print(i)

####Exemplo do codigo no intervalo de zero ate n



####3.9 - Percorrendo intervalos de zero ate n com range()

for i in range(11):
  print(i)

print(range(11-1))

####Exemplo do tipo que é range

#Gerar lista com (fim)
print(list(range(11)))

for i in range(11):
  print(i)

#Gerar com(inicio, fim)
print(list(range(12,22)))

for i in range(12,22):
  print(i)

#Gerar com (inicio, fim, passo)
print(list(range(10,200,9)))

for i in range(10,39,9):
  print(i)

# import math
num1 = int(input("Digite o primeiro numero: "))
num2  = int(input("Digite o segundo numero: "))
num3  = int(input("Digite o terceiro numero: "))

soma = ((num1 + num2) * num3)

print(range(soma))



####3.10 Enumerando coleções com for e função enumerate

impostos = ['MEI - micro empreendedor individual','ICMS - Imposto sobre Operações relativas','Imposto sobre Transmissão Causa mortis e Doação','IPI - Imposto sobre Produtos Industrializados','IOF - Imposto sobre Operações Financeiras','IRPF -  restituição de Imposto de Renda de Pessoas Físicas ','CSLL - Contribuição Social Sobre o Lucro Líquido']

for imposto in enumerate(impostos):
  print(imposto)

# salario = [1234,2032,3421,4567,5890]
a = int(input("Digite o primeiro numero a: ")) #44 + 46 = 90 / 2 = 45
b = int(input("Digite o segundo numero b: "))
c = int(input("Digite o terceiro numero c: "))

salario = [a + b,b + c, c + a]

for i in enumerate(salario):
  print(i)

####3.11 declarando funções comando def

def sum(a,b):
  return a + b

c = sum(1,3)
print(c)

####3.12 Valores padronizados de argumentos

def salario_desconto(salario2,imposto = 27.):
  return salario2 - (salario2 * (imposto * 0.01))

print(f'O valor do salario eh: {salario_desconto(5000)}')

####exemplo pratica do função def

def calcular(pa,pg,sn):
  pa = int(input("Digite o primeiro numero a: ")) #44 + 46 = 90 / 2 = 45
  pg = int(input("Digite o segundo numero b: "))
  sn = int(input("Digite o terceiro numero c: "))
  soma = pa + pg + sn
  return soma

# soma = pa + pg + sn
print(f"O resultado dos tres numero eh: {calcular(2,3,4)}")


####3.13 Parâmetros nomeados

print(f"O salario do desconto eh: {salario_desconto(salario2=5000)}")
print(f"O salario do desconto eh: {salario_desconto(4000, imposto=0.1)}")
print(f"O salario do desconto eh: {salario_desconto(5000, imposto = 0.1)}")
print(f"O salario do desconto eh: {salario_desconto(6000, imposto = 0.1)}")
print(f"O salario do desconto eh: {salario_desconto(7000, imposto = 0.1)}")
print(f"O salario do desconto eh: {salario_desconto(8000, imposto = 0.1)}")
print(f"O salario do desconto eh: {salario_desconto(9000, imposto = 0.1)}")



####3.14 Recebendo um número arbitrário de argu- mentos: packing & unpacking

from datetime import date
d = (2019,3,5)
date(d[0], d[1], d[2])

####packing

from datetime import date
d = (2019,3,5)
date(*d)

def new_user(activate=False, admin=False):
  print(activate)
  print(admin)

config = {"activate":False,
          "admin":True}
new_user(config.get('activate'), config.get('admin'))

#####Criar algo novo e mais enxuto e elegante como o codigo packing anterior só mudando a forma e ser mais enxuto e elegante

def new_user(activate=False, admin=False):
  
  print(activate)
  
  print(admin)

config = {"activate":False,
          "admin":True}

new_user(config.get('activate'), config.get('admin'))          

def new_user1(activate1 = False, admin1 = False, processador=False):
  print(activate1)
  print(admin1)
  print(processador)

config1 = {"activate1" : False,
           "admin1" : True,
           'processador':False}
new_user1(**config1)

####Unpacking dos argumentos



# Capitulo 4: primeiro programa: download de dados da copa 2014

####4.1 dowload de arquivo de tamanho conhecido

BUFF_SIZE = 1024
def dowload_length(responsive, output, length):
  times = length / BUFF_SIZE
  if length % BUFF_SIZE > 0:
    times += 1
  for time in range(times):
    output.write(responsive.read(BUFF_SIZE))
    print("Download %d " % (((times * BUFF_SIZE)/length) * 100))

BUFF_SIZE = 1024
def dowload_length(responsive, output, length):
  times = length / BUFF_SIZE
  if length % BUFF_SIZE > 0:
    times += 1
  for time in range(int(times)):
    # In a real scenario, responsive.read and output.write would be used with actual file/network objects
    # For demonstration, we'll simulate a print, and calculate progress incrementally.
    # output.write(responsive.read(BUFF_SIZE))
    current_progress_bytes = min(length, (time + 1) * BUFF_SIZE)
    percentage = (current_progress_bytes / length) * 100
    print(f"Download {current_progress_bytes} bytes ({percentage:.2f} %)")
do = dowload_length(12,30,90)
print()

#capitulo 5:

# entidades = {
#     'instituicao' : []
# }

# # entidades = dict(instituicao = [])

entidades = dict()
entidades['empreendimento'] = 'EntidadeEmpreendimento'
print(entidades)

# del entidades['empreendimento']
# print(entidades["empreendimento"])
# ----> 1 del entidades['empreendimento']
#       2 print(entidades["empreendimento"])

# KeyError: 'empreendimento'

entidades = {
    'instituicao' :[
        ('IdInstituicao', 'bigint',
         'Identicador da instituicao-PK'),
        ('Id tipo de Instituicao')
    ]
}

# import os
# for meta_files in os.listdir('data/meta-data'):
#   print(meta_files)
