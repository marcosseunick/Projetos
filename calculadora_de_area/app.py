from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def calcular_area(poligono, valor1, valor2=None, valor3=None):
    try:
        if poligono == "quadrado":
            return valor1 ** 2
        elif poligono == "triangulo":
            if valor2 is None or valor3 is None:
                return None
            s = (valor1 + valor2 + valor3) / 2
            return math.sqrt(s * (s - valor1) * (s - valor2) * (s - valor3))
        elif poligono == "retangulo":
            return valor1 * valor2
        elif poligono == "pentagono":
            return (5 / 4) * valor1**2 * (1 / math.tan(math.pi / 5))
        elif poligono == "hexagono":
            return (3 * valor1**2 * math.sqrt(3)) / 2
        elif poligono == "heptagono":
            return (7 / 4) * valor1**2 * (1 / math.tan(math.pi / 7))
        elif poligono == "octogono":
            return 2 * (1 + math.sqrt(2)) * valor1**2
        else:
            return None
    except:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    if not data or "poligono" not in data:
        return jsonify({"error": "Dados inválidos"}), 400

    poligono = data.get("poligono")
    valores = [data.get("valor1"), data.get("valor2"), data.get("valor3")]
    try:
        valores = [float(v) if v is not None else None for v in valores]
    except (ValueError, TypeError):
        return jsonify({"error": "Valores inválidos"}), 400

    area = calcular_area(poligono, *valores)
    if area is None:
        return jsonify({"error": "Polígono ou valores inválidos"}), 400
    
    return jsonify({"area": round(area, 2)})

if __name__ == '__main__':
    app.run(debug=True)
