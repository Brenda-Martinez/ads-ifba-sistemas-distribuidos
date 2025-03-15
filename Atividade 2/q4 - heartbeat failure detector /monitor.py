import time
import socket
import threading

HOST = "127.0.0.1"  # o monitor estará escutando os heartbeats localmente
PORT = 5000  # o monitor recebera os heartbeats atraves dessa porta
TIMEOUT = 10  # tempo limite para considerar um nó como falho

nodes_status = {}  # armazena o ultimo tempo que cada no enviou um heartbeat
lock = threading.Lock()  # evita que multiplas threads modifiquem o dicionario


def receive_heartbeat():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))  # cria um socket UDP para escutar as mensagens
        print("Aguardando Heartbeats...")

        while True:
            data, addr = s.recvfrom(1024)  # recebe a mensagem
            message = data.decode()
            node_id = int(message.split()[-1])  # extrai o node_id da string enviada

            with lock:
                nodes_status[node_id] = time.time()  # armazena o tempo do ultimo heartbeat para rastrear a atividade
            print(f"Recebido heartbeat de Node {node_id}")


def check_failures():
    while True:
        time.sleep(1)  # verifica a cada segundo
        current_time = time.time()
        with lock:
            for node_id in list(nodes_status.keys()):  # verifica cada no na lista
                if current_time - nodes_status[node_id] > TIMEOUT:  # se nao enviou nenhuma mensagem dentro do timeout
                    print(f"No {node_id} falhou! Nenhum heartbeat recebido.")
                    handle_failure(node_id)  # inicia a reacao a falha
                    del nodes_status[node_id]  # remove o no da lista


# obs.: essa reacao eh apenas uma simulacao para os prints
def handle_failure(node_id):
    print(f"O servidor do no {node_id} foi interrompido.")
    available_nodes = [n for n in nodes_status.keys() if n != node_id]  # verifica os nos ativos na lista
    if available_nodes:
        new_target = min(available_nodes)  # seleciona o no de menor ID
        print(f"Pedidos de compra redirecionados para o no {new_target}.\n")  # redireciona os pedidos de compra
    else:
        print("Critico: nenhum no disponivel para redirecionamento.\n")  # se nao tiver nos ativos, envia alerta critico


threading.Thread(target=receive_heartbeat, daemon=True).start()  # cria uma thread para receber mensagens
threading.Thread(target=check_failures, daemon=True).start()  # cria uma thread para verificar falhas

while True:
    time.sleep(1)
