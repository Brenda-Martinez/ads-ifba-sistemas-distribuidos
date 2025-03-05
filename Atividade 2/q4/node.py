import time
import socket
import sys
import random

HOST = "127.0.0.1"  # envia os heartbeats localmente
PORT = 5000  # envia os heartbeats atraves dessa porta
INTERVAL = 5  # envia um heartbeat a cada 5 segundos

if len(sys.argv) != 2:  # mensagem de erro caso o usuario esqueca de atribuir um ID
    print("Para ligar um servidor/no utilize: python node.py <node_id>")
    sys.exit(1)

node_id = int(sys.argv[1])  # o id do no eh definido pelo terminal pelo usuario


def send_heartbeat():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # cria um socket UDP para envio de mensagens
        while True:
            try:
                message = f"Heartbeat from Node {node_id}".encode()  # envia o heartbeat
                s.sendto(message, (HOST, PORT))  # local que recebe o heartbeat
                print(f"Heartbeat enviado")
            except Exception as e:
                print(f"Falha ao enviar Heartbeat: {e}")

            time.sleep(INTERVAL + random.uniform(-1, 1))  # variacao no tempo de envio para evitar que todos os nós
            # enviem mensagens ao mesmo tempo

send_heartbeat()



