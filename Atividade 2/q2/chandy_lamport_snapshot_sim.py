import time
from JogadorProcess import JogadorProcess


def chandy_lamport_snapshot_sim():
    p1 = JogadorProcess(1)
    p2 = JogadorProcess(2)
    p3 = JogadorProcess(3)

    # simulacao estabelecendo as conexoes entre os processos
    p1.add_channel(p2)
    p1.add_channel(p3)
    p2.add_channel(p1)
    p2.add_channel(p3)
    p3.add_channel(p1)
    p3.add_channel(p2)

    print("\nRecebendo mensagens. . .\n")
    print(". . . . . . . . . . . . . .\n")
    print("Enviando mensagens. . .\n")
    p1.send_message(p2, "Ataque")
    p2.send_message(p3, "Defesa")
    p3.send_message(p1, "Toma Pocao")

    time.sleep(1)
    p2.initiate_snapshot() # processo 2 inicia o snapshot

    time.sleep(1)
    print("\nRecebendo mensagens. . .\n")
    print(". . . . . . . . . . . . . .\n")
    print("Enviando mensagens. . .\n")
    p1.send_message(p3, "Toma Pocao")
    p2.send_message(p3, "Defesa")
    p3.send_message(p2, "Vida baixa. Use a poção!")
    p3.send_message(p1, "Ataque")

    time.sleep(1)

    # saida: estado global
    p1.show_snapshot()
    p2.show_snapshot()
    p3.show_snapshot()

if __name__ == "__main__":
    chandy_lamport_snapshot_sim()
