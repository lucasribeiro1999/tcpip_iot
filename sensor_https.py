import requests
import json
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://localhost:8443/sensores"

dados = {
    "dispositivo": "sensor_tcpip_01",
    "temperatura": 28.7,
    "umidade": 65,
    "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
}

resposta = requests.post(url, json=dados, verify=False)

print("Dados enviados via HTTPS/TLS:")
print(json.dumps(dados, indent=4, ensure_ascii=False))
print("Status da resposta:", resposta.status_code)
print("Resposta do servidor:", resposta.text)