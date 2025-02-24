import grpc
import produtos_pb2
import produtos_pb2_grpc

def cliente():
    # leitura da porta usada pelo servidor a partir do arquivo
    with open("server_port.txt", "r") as file:
        port = file.read().strip()

    host = "localhost"
    print(f"Conectando ao servidor em {host}:{port}...")

    with grpc.insecure_channel(f"{host}:{port}") as channel:
        stub = produtos_pb2_grpc.ProdutoServiceStub(channel)

        print("Conexão estabelecida. Você pode enviar comandos ao servidor.")
        print("Comandos disponíveis:")
        print("1 - Consultar produto (NOME)")
        print("2 - Consultar produtos (PRECO MAXIMO)")
        print("3 - Atualizar estoque")
        print("4 - Listar todos os produtos")
        print("5 - Sair")

        while True:
            escolha = input("Digite sua escolha: ").strip()
            if escolha == "1":
                nome = input("Digite o nome do produto: ").strip()
                try:
                    response = stub.ConsultarProdutoNome(produtos_pb2.ProdutoRequest(nome=nome))
                    produto = response.produto
                    print(f"{produto.nome}: R${produto.preco}, Estoque: {produto.quantidade}")
                except grpc.RpcError as e:
                    print(f"Erro: {e.details()}")
            elif escolha == "2":
                preco = float(input("Digite o preço máximo: ").strip())
                response = stub.ConsultarProdutoPreco(produtos_pb2.PrecoRequest(preco_max=preco))
                for produto in response.produtos:
                    print(f"{produto.nome}: R${produto.preco}, Estoque: {produto.quantidade}")
            elif escolha == "3":
                nome = input("Digite o nome do produto: ").strip()
                quantidade = int(input("Digite a quantidade a ser atualizada: ").strip())
                try:
                    response = stub.AtualizarEstoque(produtos_pb2.AtualizarRequest(nome=nome, quantidade=quantidade))
                    print(response.mensagem)
                except grpc.RpcError as e:
                    print(f"Erro: {e.details()}")
            elif escolha == "4":
                response = stub.ListarProdutos(produtos_pb2.Empty())
                for produto in response.produtos:
                    print(f"{produto.nome}: R${produto.preco}, Estoque: {produto.quantidade}")
            elif escolha == "5":
                print("Encerrando o cliente...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    cliente()
