class LamportClock:
    def __init__(self, node_id):
        self.node_id = node_id  # identificador unico
        self.clock = 0  # Contador logico. OBS timestamp é o valor de self.clock no momento do envio de uma mensagem

    def increment(self):
        self.clock += 1  # incrementa o relogio

    def send_event(self):
        self.increment()  # incrementa o relogio antes do envio
        print(f"Nó {self.node_id} enviou uma mensagem com timestamp {self.clock}")  # simulacao da mensagem
        return self.clock  # retorna o timestamp da mensagem

    def receive_event(self, received_clock):
        self.clock = max(self.clock, received_clock) + 1  # atualiza o relogio p garantir a ordem causal
        print(f"Nó {self.node_id} recebeu uma mensagem. Novo relógio: {self.clock}")
