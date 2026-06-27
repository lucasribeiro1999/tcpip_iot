from app_base import app

if __name__ == "__main__":
    print("Servidor HTTPS iniciado em https://localhost:8443")
    app.run(
        host="0.0.0.0",
        port=8443,
        ssl_context=("cert.pem", "key.pem")
    )