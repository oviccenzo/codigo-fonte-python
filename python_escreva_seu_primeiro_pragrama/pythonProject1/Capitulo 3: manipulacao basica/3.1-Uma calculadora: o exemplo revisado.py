#Capitulo 3:Manipulações básicas

####3.1 Uma calculadora: o exemplo revisado

imposto = 0.27
salario = 5000
print("Salario real: {}".format(salario - (salario * imposto)))
print("Imposto: {}".format(salario * imposto))

imposto = 0.27
salario = 3000
print("Valor real: {0}".format(salario - (salario * imposto)))

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

5# salario = [1234,2032,3421,4567,5890]
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

####3.14 recebendo um numero arbitrario de argumentos: packing & unpacking

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

#####3.15 usando código já pronto: importando módulos

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