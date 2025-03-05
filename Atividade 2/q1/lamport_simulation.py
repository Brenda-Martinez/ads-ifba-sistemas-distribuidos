import time
import random
from LamportClock import LamportClock

def lamport_simulation():
    node1 = LamportClock(1)
    node2 = LamportClock(2)
    node3 = LamportClock(3)

    # simulacao de eventos
    for _ in range(5):
        sender, receiver = random.sample([node1, node2, node3], 2)  # seleciona aleatoriamente 2 nos
        sender.increment()  # incrementa o relogio do sender
        print(f"Nó {sender.node_id} executou um evento local. Timestamp: {sender.clock}")  # realiza evento
        msg_clock = sender.send_event()  # sender envia o evento e retorna o timestamp
        receiver.receive_event(msg_clock)  # receiver recebe a mensagem e atualiza o relogio
        print("\n------ (Aguardando nova mensagem ...) ------\n")
        time.sleep(1)

if __name__ == "__main__":
    lamport_simulation()

