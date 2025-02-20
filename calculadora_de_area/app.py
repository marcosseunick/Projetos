from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        data = request.get_json()

        if not data or "poligono" not in data:
            return jsonify({"error": "Dados inválidos"}), 400

        poligono = data.get("poligono")
        valor1 = data.get("valor1")
        valor2 = data.get("valor2", None)  

        try:
            valor1 = float(valor1)
        except (ValueError, TypeError):
            return jsonify({"error": "Valor inválido para cálculo"}), 400

    
        if poligono in ["triangulo", "retangulo"]:
            try:
                valor2 = float(valor2)
            except (ValueError, TypeError):
                return jsonify({"error": "Altura/Base inválida"}), 400
        else:
            valor2 = None 

        area = None

        if poligono == "quadrado":
            area = valor1 ** 2
        elif poligono == "triangulo":
            area = (valor1 * valor2) / 2
        elif poligono == "retangulo":
            area = valor1 * valor2
        elif poligono == "hexagono":
            area = (3 * valor1**2 * math.sqrt(3)) / 2
        else:
            return jsonify({"error": "Polígono inválido"}), 400

        return jsonify({"area": round(area, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500 

if __name__ == '__main__':
    app.run(debug=True)
