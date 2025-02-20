from time import sleep
import math

def validar_entrada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 1:
                return valor
            print("Valor inválido. Deve ser maior ou igual a 1.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def calcular_area(poligono):
  if poligono == "quadrado":
    l = validar_entrada("Digite o tamanho de um lado do quadrado: ")
    return l * l

  elif poligono == "triangulo":
    b = validar_entrada("Digite o Valor da Base: ")
    h = validar_entrada("Digite o Valor da Altura: ")
    return (b*h)/2

  elif poligono == "retangulo":
    b = validar_entrada("Digite o valor da base: ")
    h = validar_entrada("Digite o valor da altura: ")
    return b * h

  elif poligono == "hexagono":
    l = validar_entrada("Digite o tamanho de um lado do hexágono: ")
    return (3 * l**2 * math.sqrt(3)) / 2

  return None
  
sleep(2)
print(f"{'=-=' * 10}")
print("\033[37;44mCalculadora de Área de Poligonos\033[m")
print(f"{'=-=' * 10}")
sleep(2)

while True:
    poligono = input("Digite qual polígono você quer saber a área: ").strip().lower()
    
    area = calcular_area(poligono)

    if area is not None:
        print("ANALISANDO...")
        sleep(2)
        print(f"A área do {poligono} é {area:.2f}")
        break
    else: 
        print("Polígono inválido, tente novamente!")