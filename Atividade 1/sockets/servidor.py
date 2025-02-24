import socket

catalogo_produtos = {
    "Maca": {"preco": 3, "quantidade": 20},
    "Pera": {"preco": 5, "quantidade": 15},
    "Banana": {"preco": 10, "quantidade": 30},
    "Caju": {"preco": 2, "quantidade": 60}
}

def listar_produtos():
    retorno = "Produtos disponíveis:\n"
    for produto, detalhes in catalogo_produtos.items():
        retorno += f"- {produto}: Preço R$ {detalhes['preco']} | Quantidade: {detalhes['quantidade']}\n"
    return retorno

def consultar_produto_nome(nome):
    produto = catalogo_produtos.get(nome)
    if produto:
        return f"{nome}: Preço R$ {produto['preco']} | Quantidade: {produto['quantidade']}\n"
    else:
        return f"Produto '{nome}' não encontrado no catálogo.\n"

def consultar_produto_preco(preco_max):
    retorno = f"Produtos com preço até R$ {preco_max}:\n"
    encontrados = False
    for produto, detalhes in catalogo_produtos.items():
        if detalhes['preco'] <= preco_max:
            retorno += f"- {produto}: Preço R$ {detalhes['preco']} | Quantidade: {detalhes['quantidade']}\n"
            encontrados = True
    if not encontrados:
        retorno += "Nenhum produto encontrado nessa faixa de preço.\n"
    return retorno

def atualizar_estoque(nome, quantidade):
    produto = catalogo_produtos.get(nome)
    if produto:
        produto['quantidade'] += quantidade
        return f"Estoque atualizado para '{nome}'. Nova quantidade: {produto['quantidade']}\n"
    else:
        return f"Produto '{nome}' não encontrado no catálogo.\n"

def servidor(host = 'localhost', port = 8082):
    data_max = 2048  # maximo de dados a serem recebidos de uma vez
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AFINET eh enderecos ipv4, SOCK STREAM eh prot TCP

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # permite reusar endereco e porta

    server_address = (host, port)  # liga o socket na porta indicada
    print ("Iniciando comunicacao com %s na porta %s" % server_address)
    sock.bind(server_address)
    sock.listen(5)  # 5 conexoes serao enfileiradas antes do accept, nao espero receber mais que 5 conexoes
    i = 0
    while True:
        print("Aguardando conexão...")
        connection, client_address = sock.accept()
        try:
            print(f"Conexão estabelecida com {client_address}")

            while True:
                data = connection.recv(data_max).decode()  # o metodo decode converte os dados recebidos em formato binario (bytes) para uma string
                if not data:
                    break

                print(f"Comando recebido: {data}")

                # tratamento dos comandos recebidos
                partes = data.split()
                comando = partes[0]

                if comando == "1":
                    nome = " ".join(partes[1:])
                    response = consultar_produto_nome(nome)
                elif comando == "2":
                    preco = float(partes[1])
                    response = consultar_produto_preco(preco)
                elif comando == "3":
                    nome = partes[1]
                    quantidade = int(partes[2])
                    response = atualizar_estoque(nome, quantidade)
                elif comando == "4":
                    response = listar_produtos()
                else:
                    response = "Comando não reconhecido.\n"

                connection.sendall(response.encode())  # envia a resposta/retorno do comando para o cliente
        finally:
            connection.close()
            i += 1
            if i >= 3:
                print(f"Numero max de conexoes atingidas.")
                break  # se chegar a 3 conexoes o servidor eh encerrado

servidor()