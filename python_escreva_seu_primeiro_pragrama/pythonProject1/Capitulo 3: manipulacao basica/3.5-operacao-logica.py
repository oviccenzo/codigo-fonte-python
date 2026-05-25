####3.5 Operações logicos

imposto6 = float(input("Imposto? "))
if imposto6 < 10:
  print("baixo")
elif imposto6 >= 10. and imposto6 <= 27.:
  print("medio")
elif imposto6 > 27. and imposto6 < 100:
  print("alto")
else:
  print("imposto invalido")