import random
from Process import Process


def bully_sim():
    num_processes = 5
    processes = [Process(i, []) for i in range(1, num_processes + 1)]  # cria os processos / nos
    for p in processes:
        p.processes = processes  # lista de processos

    random.choice([p for p in processes if p.alive]).start_election(processes)  # no aleatorio inicia a eleicao

    leader = next((p for p in processes if p.is_leader), None)

    if leader:
        leader.fail()  # simula falha

    if leader:
        leader.recover()  # simula recover


if __name__ == "__main__":
    bully_sim()
