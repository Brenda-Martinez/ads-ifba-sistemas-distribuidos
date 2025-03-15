import random


class JogadorProcess:
    def __init__(self, process_id):
        self.process_id = process_id  # identificador unico
        self.state = {  # estado inicial representado por numeros aleatorios
            "vida": random.randint(50, 100),
            "pontuacao": random.randint(0, 2000),
            "itens": random.choices(["espada", "escudo", "poção", "arco", "flecha"], k=2)
        }
        self.channels = {}  # conexoes com outros processos
        self.received_marker = False  # indica se ja recebeu um marcador
        self.recorded_state = None  # guarda o estado salvo no snapshot
        self.channel_messages = {}  # armazena mensagens recebidas depois do primeiro marcador

    def add_channel(self, neighbor):
        self.channels[neighbor.process_id] = neighbor  # adiciona um processo vizinho na rede
        self.channel_messages[neighbor.process_id] = []  # inicializa buffer que armazena as mensagens

    def send_message(self, receiver, message):  # envia uma mensagem de um processo (jogador) p outro
        print(f"Jogador {self.process_id} enviou '{message}' para Jogador {receiver.process_id}")
        receiver.receive_message(self.process_id, message)

    def receive_message(self, sender_id, message):
        if self.received_marker:  # se o snapshot tiver sido iniciado
            self.channel_messages[sender_id].append(message)  # a mensagem eh armazenada no buffer
        print(f"Jogador {self.process_id} recebeu '{message}' de Jogador {sender_id}")

    def initiate_snapshot(self):
        print(f"\n[SNAPSHOT] Jogador {self.process_id} iniciou a captura de estado global\n")
        self.recorded_state = self.state.copy()  # o processo salva o estado global
        self.received_marker = True
        self.send_marker()  # o marcador eh enviado para os vizinhos

    def send_marker(self):
        for neighbor_id, neighbor in self.channels.items():
            print(f"Jogador {self.process_id} enviou MARCADOR para Jogador {neighbor_id}")
            neighbor.receive_marker(self.process_id)

    def receive_marker(self, sender_id):
        if not self.received_marker:  # se o processo nunca recebeu o marcador antes
            self.recorded_state = self.state.copy()  # o processo salva o estado glocal
            self.received_marker = True
            print(f"Jogador {self.process_id} recebeu MARCADOR de {sender_id} e salvou estado: {self.recorded_state}")
            self.send_marker()  # o marcador eh enviado para os vizinhos
        else:
            print(f"Jogador {self.process_id} ignorou MARCADOR de {sender_id}, pois já recebeu anteriormente")

    def show_snapshot(self):
        print(
            f"\n[ESTADO GLOBAL] Jogador {self.process_id}: Estado = {self.recorded_state}, Canais = {self.channel_messages}")
