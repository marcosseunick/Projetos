from time import sleep
import math 
print(f"{'=-=' * 10}")
print("\033[37;44mCalculadora de Área de Poligonos\033[m")
print(f"{'=-=' * 10}")
while True:
  poligono = str(input("Digite qual poligono você quer saber a área: "))

  if poligono == "quadrado":
    l = float(input("Digite o tamanho de um lado do quadrado: "))
    while l < 1:
     print("Tamanho Inválido")
     sleep(1)
     l = float(input("Digite o tamanho de um lado do quadrado: "))
    a = l * l 
    print("ANALISANDO...")
    sleep(2)
    print("A área do quadrado é: ", a)
  
  elif poligono == "triangulo":
    b = float(input("Digite o valor da base: "))
    while b < 1:
      print("Valor Inválido")
      sleep(1)
      b = float(input("Digite o valor da base: "))
    h = float(input("Digite o valor da altura: "))
    while h < 1:
      print("Valor Inválido")
      sleep(1)
      h = float(input("Digite o valor da altura: "))
    a = (b*h)/2
    print("ANALISANDO...")
    sleep(2)
    print("A área do triângulo é: ", a)
  
  elif poligono == "retangulo":
    b = float(input("Digite o valor da base: "))
    while b < 1:
      print("Valor Inválido")
      sleep(1)
      b = float(input("Digite o valor da base: "))
    h = float(input("Digite o valor da altura: "))
    while h < 1:
      print("Valor Inválido")
      sleep(1)
      h = float(input("Digite o valor da altura: "))
    a = b * h
    print("ANALISANDO...")
    sleep(2)
    print("A área do retângulo é:", a)

  elif poligono == "hexagono":
    l = float(input("Digite o tamanho de um lado do hexágono: "))
    while l < 1:
      print("Valor Inválido")
      sleep(1)
      l = float(input("Digite o tamanho de um lado do hexágono: "))
    a = (3 * l**2 * math.sqrt(3)) / 2
    print("ANALISANDO...")
    sleep(2)
    print("A área do hexágono é:", a)

  else:
    print("Polígono Inválido")
    continue
  break