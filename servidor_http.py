from app_base import app

if __name__ == "__main__":
    print("Servidor HTTP iniciado em http://localhost:8080")
    app.run(host="0.0.0.0", port=8080)
    