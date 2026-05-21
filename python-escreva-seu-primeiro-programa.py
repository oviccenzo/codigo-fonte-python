#pratica

num1 = int(input("Digite qualquer numero inteiro: "))
num2 = 27

while num2 > 0:
  num2 = (input("Digite qualquer numero inteiro ou (0) para sair: "))
  if not num2:
    num2 = 27.
  else:
    num2 = float(num2)
  print("O valor real do numero eh: {0}".format(num1 - (num1 * (num2 * 0.01))))

salario1 = int(input("Salario?: "))
imposto1 = 27. 
while imposto1 > 0:
  imposto1 = (input("Imposto ou (0) para sair: "))
  if not imposto1:
    imposto1 = 27.
  else:
    imposto1 = float(imposto1)
  print("Valor real: {0}".format(salario1 - (salario1 * (imposto1 * 0.01))))

saldo = float(input("Digite o saldo: "))
salario = float(input("Digite o salario: "))

totalDoSalario = saldo * salario

print(f"O total do saldo com porcentagem é: {totalDoSalario}")

complex(12 + 2, 2 + 20) #n1 + n2 , n2 + n1 

n1 = int(input("Digite o primeiro numero -> n1: "))
n2 = int(input("Digite o segundo numero -> n2: "))
n3 = int(input("Digite o terceiro numero -> n3: "))
n4 = int(input("Digite o quarto numero -> n4: "))

complex(n1 + n2 + n3 + n4)

print(f"O numero de n1 eh: {n1}")
print(f"O numero de n2 eh: {n2}")
print(f"O numero de n3 eh: {n3}")
print(f"O numero de n4 eh: {n4}")

somaTotal = n1 + n2 + n3 + n4

print(f"O numero complexo é: {complex(n2 + n3+ n1 + n4, n2 + n1 +n3 + n4) }")
print(f"A soma total é: {somaTotal}")

st = 'ola mundo'

st[0]

st[1:4]

st[2:]

st[:3]

len(st)

st = 'python 4'

len(st)

st = 'ola meu nome é viccenzo de oliveira nunes resende , eu sou pcda'

len(st)

# Capitulo 1: Iniciando com python

1.5 primeiros passo abra o interpretador

!python --version

1.6 primeira exploração

1

3/2

print("hello world")

# Capitulo 2: aprendendo python na prática números e strings

2.1-numeros

print(1) #int

print(1.0) #float

print(1.) #float tambem

print(1+2j) #complex

####Gerando numeros por meios das funções embutidos

int(1.0)

int('9')

float(1)

float('9.2')

float('-inf')

float('+inf')

float('nan')

complex(1,2)

####ints e longs unificando no python 3 

Alguns exemplos de números e manipulações simples

print(3 + 2)

print(3 + 4.2)

print(4/2)

print(5/2)

print(5//2)

print(complex(1,2) + 2)

print(complex(2,0) + 0 + 1j)

print(2 + 0 + 1j)

####operadores aritmeticas

print(1 + 2)

print(3 - 1)

print(10/2)

print(10//3)

print(10 * 2 + 1)

print(10 % 3)

print(-3)

print(2 ** 8)

####operadores de bits

print(1|0)

print(1 | 5)

print(1^5)

print(4 & 1)

print(1 << 2)

print(4 >> 2)

print(~4)

####operações misturando tipos diferentes e as regras de coerção

print(100* 1.3) #preço mais 30%

type(1 + 2.0)

type(1+2j)

type(1.0+2j)

type(1.0+1.0)

####2.3-Criando e maniupulando texto: strings

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
      'para a população: ')

####len(strings), explicação len e para o tamanho da string

st = "macarana"

st[0]

st[1:4]

st[2:]

st[:3]

len(st)

####Sequencias string

print("m" in "macarana")

print("x" not in "macarana")

("m" +"aracana")

"a" * 3

####imutabilidade: novas strings criadas a partir de outras strings

minha_str = "livro python 3"
print(minha_str[13] + "2")

####copiando e manipulando texto com a string

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

####interpolando a string

(("%d dias para copa") % (100))

"{} dias para copa".format(100)

"{dia} dias para copa".format(dia=100)

"{:<60}".format("alinhados á esquerda, ocupando 60 posições")

"{:>60}".format("alinhados á esquerda, ocupando 60 posições")

"{:^60}".format("centralizados á esquerda, ocupando 60")

####operações misturados tipos diferentes e as regras de coerção

print(100 * 1.3) #preço mais de 30%

####explorando as operações por conta propria

type(1 + 2.0)

type(1 + 2j)

type(1.0 + 1.0)

#Capitulo 3:Manipulações básicas

####3.1 Uma calculadora: o exemplo revisado

imposto = 0.27
salario = 5000
print("Salario real: {}".format(salario - (salario * imposto)))
print("Imposto: {}".format(salario * imposto))

3.1.1

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

# print(10 >1j) possui o erro esse codigo

####3.4-Condicionais if else elif e else

salario1 = int(input("Salario? "))
imposto1 = float(input("Imposto? "))
if imposto1 == '':
  imposto1 = 27.5
else:
  imposto1 = float(imposto1)
print("Valor real: {0}".format(salario1 - (salario1 * (imposto1 * 0.01))))

indentação dos blocos de códigos

imposto2 = float(input("Imposto? "))
if imposto2 < 10:
  print("Medio")
elif imposto2 < 27.5:
  print("Alto")
else:
  print("Muito alto")

comando if

salario3 = int(input("Salario? "))
imposto3 = float(input("Imposto em % (exemplo: 27.5)? "))

if not imposto3:
  imposto3 = 27.5
else:
  imposto3 = float(imposto3)

print("Valor real: {0}".format( salario3 * (imposto3 * 0.01)))

Expressão if

imposto4 = 0.3
"alto" if imposto4 > 0.27 else "baixo"

imposto5 = 0.10
"alto" if imposto5 > 0.27 else "baixo"

valor_imposto = "alto" if imposto > 0.27 else "baixo"
print(valor_imposto)


3.5 Operações logicos

imposto6 = float(input("Imposto? "))
if imposto6 < 10:
  print("baixo")
elif imposto6 >= 10. and imposto6 <= 27.:
  print("medio")
elif imposto6 > 27. and imposto6 < 100:
  print("alto")
else:
  print("imposto invalido")


3.6 - loops com while

salario7 = float(input("Salario? "))
imposto7 = 27.
while imposto7 > 0:
  imposto7 = (input("Imposto ou (0) para sair: "))
  if not imposto7:
    imposto7 = 27.
  else:
    imposto7 = float(imposto7)
  print("Valor real: {0} ".format(salario7 - (salario7 * (imposto7 * 0.01))))

o loop pode ser interrompido com um comando o break que é quebrar linha

salario8 = float(input("Salario? ")) #esse linha falar para digitar qualquer valor do salario
imposto8 = 27 #esse imposto tem o valor de 27
while imposto8 > 0:
  imposto8 = input("Imposto ou (s) para sair: ")
  if not imposto8:
    imposto = 27.
  elif imposto8 == 's':
    break
  else:
    imposto8 = float(imposto8)
  print("Valor real: {0} ".format(salario8 - (salario8 * (imposto8 * 0.01))))


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

lista =["impostos","salarios","altos","baixos"]
(lista[0] , lista[1] , lista[2] , lista[3])

####lista são mutaveis

lista = ["impostos","salarios","altos","baixos"]
(lista[0] ,lista[1] ,lista[2], lista[3])

####ifs e listas

lista = []

if lista:
  print("Nunca sou executado")
else:
  print("Sempre sou executado")

####3.8 loop pythônicos com for e listas

impostos9 = ["MEI","Simples"]
for imposto in impostos9:
  print(impostos9)

####comando for em detalhe

lista = [0,1,2,3,4,5,6,7,8,9,10]

for i in lista:
  print(i)

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

def sum(a,b,c):
  return a + b + c #+ c

c1 = sum(1,3,4)
print(c1)

####3.12 valores padronizados de argumentos

def salarioDescontadoImposto1(salario9, imposto9 = 27.):
  return salario9 - (salario9 * (imposto9 * 0.01))

salarioDescontadoImposto1(5000)

####3.13 parametros nomeados

print(salarioDescontadoImposto1(1000, imposto9 = 0.10))
print(salarioDescontadoImposto1(2000, imposto9 = 0.10))
print(salarioDescontadoImposto1(3000, imposto9 = 0.10))
print(salarioDescontadoImposto1(4000, imposto9 = 0.10))
print(salarioDescontadoImposto1(5000, imposto9 = 0.10))
print(salarioDescontadoImposto1(6000, imposto9 = 0.10))

###3.14 recebendo um numero arbitrario de argumentos: packing & unpacking

from datetime import date

d = (2013, 3 , 15)
date(d[0], d[1], d[2])

####exemplo 1: que é o packing que está na mesmo ordem só mudando o codigo

from datetime import date
d = (2013, 3 , 15)
date(*d)

####exemplo 2: a configuração do administrador ou ativo , verdade ou falso

def novoUso(active = True, admin = False):
  print(active)
  print(admin)

config = {"active": False,
          "admin" : True}

novoUso(config.get("active"),config.get("admin"))


####exemplo 3: o mesmo codigo só mudando linha do codigo para ficar mais exunto e elegante

def novoUso(active = True, admin = False):
  print(active)
  print(admin)

config = {"active" : False , "admin" : True }

novoUso(**config)

####Exemplo 4: unpacking dos argumentos

def unpackingExperiment(*args):
  args1 = args[0]
  args2 = args[1]
  other = args[2:]
  print(args1)
  print(args2)
  print(other)

unpackingExperiment(1,2,3,4,5,6)

####Exemplo 5: kwargs dos argumentos

def unpackingExperiment(**kwargs):
  print(kwargs)

unpackingExperiment(named="Teste", other = "Other")

####3.15 usando código já pronto: importando módulos

import math
print(math.sqrt(9))

####exemplo do erro

# import math
# math = 10
# print(math.sqrt(9))
# exemplo do erro
# AttributeError                            Traceback (most recent call last)

# /tmp/ipython-input-4096810097.py in <cell line: 0>()
#       1 import math
#       2 math = 10
# ----> 3 print(math.sqrt(9))

# AttributeError: 'int' object has no attribute 'sqrt'

####exemplo 3 criar um modulo alia ou um objeto importado

import math as matematica

print(matematica.sqrt(9))

####exemplo 4: importar apenas um objetos especifico para uso do objeto que é from o modulo e depois o import que importar

from unittest import TestCase as tc

print(tc)

from math import log2 as l2

print(l2(1024))

# Capitulo 4: primeiro programa: download de dados da copa 2014

4.1 criando uma função para fazer dowloada no navegador da web e ler o tamanho do arquivos

##indereço do buffe size
BUFF_SIZE = 1024
def dowloadLength(response, output, length):
  times = length / BUFF_SIZE
  if length % BUFF_SIZE > 0:
    times += 1
  for time in range(times):
    output.write(response.read(BUFF_SIZE))
    print("Dowloaded %d " % (((time * BUFF_SIZE)/length)*100))


criando outra função para download na web

def dowload(response, output):
  totalDowloaded = 0
  while True:
    data = response.read(BUFF_SIZE)
    totalDowloaded += len(data)
    if not data:
      break
    output.write(data)
    print(f"Downloaded {bytes}".format(bytes = totalDowloaded))


4.2 unindo dois programa completo para formar um só programa

# #coding: utf-8
# import io
# import sys
# import urllib.request as request

# BUFF_SIZE = 1024

# def main():
#   response = request.urlopen(sys.argv[1])
#   out_file = io.FileIO("saida.zip", mode="w")

#   content_length = response.getheader("Content-Length")
#   if content_length:
#     length = int(content_length)

4.3 definindo funções main

def main():
  print("ola")

if __name__ == "__main__":
  main()





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
