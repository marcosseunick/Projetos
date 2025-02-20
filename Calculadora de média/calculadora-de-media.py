from time import sleep

print("\033[0;30;44mCalculadora de média anual\033[m")
sleep(0.5)
b1 = float(input("Digite sua nota do primeiro bimestre: "))
b2 = float(input("Digite sua nota do segundo bimestre: "))
b3 = float(input("Digite sua nota do terceiro bimestre:"))
b4 = float(input("Digite sua nota do quarto bimestre: "))
m = (b1 + b2 + b3 + b4)/4
print("ANALISANDO...")
sleep(3)
if m < 6:
  print("Sua média é ", m,". Infelizmente você não conseguiu passar de ano.")
if m >= 6:
  print("Sua média é ", m,". Você passou! Parabéns!")