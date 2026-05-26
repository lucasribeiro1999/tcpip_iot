from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/sensores", methods=["POST"])
def sensores():
    dados = request.get_json()

    print("\n=== Dados recebidos do sensor ===")
    print("Data/hora:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("Conteúdo:", dados)

    return jsonify({
        "status": "ok",
        "mensagem": "Dados recebidos com sucesso",
        "dados_recebidos": dados
    }), 200