import socket

def cliente(host='localhost', port=8082):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (host, port)
        print(f"Conectando ao servidor em {host}: {port}...")
        sock.connect(server_address)

        print("Conexão estabelecida. Você pode enviar comandos ao servidor.")
        print("Comandos disponíveis:")
        print("1 - Consultar produto (NOME)")
        print("2 - Consultar produtos (PRECO MAXIMO)")
        print("3 - Atualizar estoque")
        print("4 - Listar todos os produtos")
        print("5 - Sair")

        while True:
            comando = input("Comando: ").strip()
            if comando == "5":
                print("Encerrando a conexão com o servidor...")
                break

            # envia o comando para o servidor
            if comando == "1":
                nome = input("Digite o nome do produto: ").strip()
                sock.sendall(f"1 {nome}".encode())
            elif comando == "2":
                preco = input("Digite o preco maximo: ").strip()
                sock.sendall(f"2 {preco}".encode())
            elif comando == "3":
                nome = input("Digite o nome do produto: ").strip()
                quantidade = input("Digite a quantidade a ser atualizada: ").strip()
                sock.sendall(f"3 {nome} {quantidade}".encode())
            elif comando == "4":
                sock.sendall("4".encode())
            else:
                print("Opcao invalida. Tente novamente.")
                continue

            # recebe a resposta do servidor
            resposta = sock.recv(2048).decode()
            print("Resposta do servidor:")
            print(resposta)

    except ConnectionRefusedError:
        print("Erro: Não foi possível conectar ao servidor. Verifique se ele está em execução.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        sock.close()
        print("Conexão encerrada.")

cliente()