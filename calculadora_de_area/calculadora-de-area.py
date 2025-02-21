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
   while True:
    a = validar_entrada("Digite o Valor do Lado a: ")
    b = validar_entrada("Digite o valor do lado b: ")
    c = validar_entrada("Digite o valor do lado c: ")
    if a + b > c and a + c > b and b + c > a:
       s = (a + b + c)/2
       area = math.sqrt(s * (s - a) * (s - b) * (s-c))
       return area
    else:
       print("Triangulo inválido. Tente novamentet")
  
  elif poligono == "retangulo":
    b = validar_entrada("Digite o valor da base: ")
    h = validar_entrada("Digite o valor da altura: ")
    return b * h
  
  elif poligono == "pentagono":
     l = validar_entrada("Digite o valor do lado do pentágono: ")
     area = ((5 / 4) * l**2 * (1 / math.tan(math.pi / 5)))
     return area

  elif poligono == "hexagono":
    l = validar_entrada("Digite o tamanho de um lado do hexágono: ")
    return (3 * l**2 * math.sqrt(3)) / 2

  elif poligono == "heptagono":
     l = validar_entrada("Digite o tamanho de um lado do Heptágono: ")
     area  = (7 / 4) * l**2 * (1 / math.tan(math.pi / 7))
     return area
  
  elif poligono == "octogono":
    l = validar_entrada("Digite o tamanho de um lado do Octógono: ")
    area  = 2 * (1 + math.sqrt(2)) * l**2
    return area

  return None

print(f"{'=-=' * 10}")
print("\033[37;44mCalculadora de Área de Poligonos\033[m")
print(f"{'=-=' * 10}")
sleep(1)

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