import random


class Process:
    def __init__(self, process_id, processes):
        self.process_id = process_id  # identificador unico
        self.processes = processes  # lista de processos
        self.is_leader = False  # indica se o processo é o líder
        self.alive = True  # indica se o processo está ativo

    def start_election(self, nodes):
        if not self.alive:
            return  # se o processo está inativo nao pode iniciar uma eleicao

        if self.is_leader:
            return  # se ja eh lider nao precisa iniciar outra eleicao

        print(f"No {self.process_id} iniciou uma eleição.")

        # lista de nos com ID maior e ativos, para garantir que apenas nos maiores estejam competindo
        higher_nodes = [node for node in nodes if node.process_id > self.process_id and node.alive]

        if not higher_nodes:  # se nao tem processos com ID maior e ativo
            self.become_leader()  # o no se proclama lider
        else:
            for node in higher_nodes:
                print(f"No {self.process_id} -> No {node.process_id}: Você tem um ID maior?")  # desafio aos nos
                response = node.respond_to_election()  # resposta se esta ativo
                if response:  # se o no estiver ativo
                    node.start_election(nodes)  # no maior e ativo controla a eleicao
                    return  # evita que vários processos tentem se tornar lider ao mesmo tempo

            self.become_leader()  # se nenhum no responder o no que iniciou a eleicao vira lider

    def respond_to_election(self):
        return self.alive  # retorna true se o processo estiver ativo

    def become_leader(self):
        self.is_leader = True  # define o processo como lider
        print(f"\nNo {self.process_id} tornou-se o novo lider!\n")
        for p in self.processes:
            if p.process_id != self.process_id:
                p.receive_leader_message(self.process_id)  # notifica todos os outros nos sobre sua eleicao

    def receive_leader_message(self, leader_id):
        print(f"No {self.process_id} reconhece no {leader_id} como lider.")
        self.is_leader = False  # o processo deixa de ser um lider

    def fail(self):
        self.alive = False  # simula uma falha no processo, desativa o no
        self.is_leader = False
        print(f"\nNo {self.process_id} falhou!\n")
        self.initiate_new_election()  # inicia uma nova eleicao

    def initiate_new_election(self):
        active_nodes = [p for p in self.processes if p.alive]
        if active_nodes:
            starter = random.choice(active_nodes)
            print(f"No {starter.process_id} foi escolhido para iniciar a nova eleição após falha de {self.process_id}.")
            starter.start_election(self.processes)

    def recover(self):
        self.alive = True  # simula uma recuperacao do processo reativando o no
        print(f"\nNo {self.process_id} voltou a funcionar.\n")
        self.start_election(self.processes)  # inicia uma nova eleicao
