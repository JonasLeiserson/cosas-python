import socket

HOST = '0.0.0.0'  
PORT = 5000       
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Esperando conexión...")
    conn, addr = s.accept()
    with conn:
        print(f"Conectado por {addr}")
        with open("logs2.txt", "wb") as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        print("Archivo recibido.")
