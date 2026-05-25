####3.4-Condicionais if else elif e else

salario1 = int(input("Salario? "))
imposto1 = float(input("Imposto? "))
if imposto1 == '':
  imposto1 = 27.5
else:
  imposto1 = float(imposto1)
print("Valor real: {0}".format(salario1 - (salario1 * (imposto1 * 0.01))))

print('\n')

# identação dos blocos de códigos.py
####indentação dos blocos de códigos
imposto2 = float(input("Imposto? "))
if imposto2 < 10:
  print("Medio")
elif imposto2 < 27.5:
  print("Alto")
else:
  print("Muito alto")

print('\n')

#comando if

salario3 = int(input("Salario? "))
imposto3 = float(input("Imposto em % (exemplo: 27.5)? "))

if not imposto3:
  imposto3 = 27.5
else:
  imposto3 = float(imposto3)

print("Valor real: {0}".format( salario3 * (imposto3 * 0.01)))

print('\n')

####Expressão if

imposto4 = 0.3
"alto" if imposto4 > 0.27 else "baixo"

imposto5 = 0.10
"alto" if imposto5 > 0.27 else "baixo"

valor_imposto = "alto" if imposto > 0.27 else "baixo"
print(valor_imposto)

print('\n')

####Expressão if

imposto4 = 0.3
"alto" if imposto4 > 0.27 else "baixo"

imposto5 = 0.10
"alto" if imposto5 > 0.27 else "baixo"

valor_imposto = "alto" if imposto > 0.27 else "baixo"
print(valor_imposto)

print('\n')

####indentação dos blocos de códigos
imposto2 = float(input("Imposto? "))
if imposto2 < 10:
  print("Medio")
elif imposto2 < 27.5:
  print("Alto")
else:
  print("Muito alto")

