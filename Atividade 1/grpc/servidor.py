import grpc
from concurrent import futures
import produtos_pb2
import produtos_pb2_grpc

catalogo_produtos = {
    "Maca": {"preco": 3, "quantidade": 20},
    "Pera": {"preco": 5, "quantidade": 15},
    "Banana": {"preco": 10, "quantidade": 30},
    "Caju": {"preco": 2, "quantidade": 60}
}

class ProdutoService(produtos_pb2_grpc.ProdutoServiceServicer):
    def ListarProdutos(self, request, context):
        produtos = [
            produtos_pb2.Produto(nome=nome, preco=dados["preco"], quantidade=dados["quantidade"])
            for nome, dados in catalogo_produtos.items()
        ]
        return produtos_pb2.ListaProdutos(produtos=produtos)

    def ConsultarProdutoNome(self, request, context):
        nome = request.nome
        if nome in catalogo_produtos:
            produto = catalogo_produtos[nome]
            return produtos_pb2.ProdutoResponse(
                produto=produtos_pb2.Produto(nome=nome, preco=produto["preco"], quantidade=produto["quantidade"])
            )
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details(f"Produto '{nome}' não encontrado.")
        return produtos_pb2.ProdutoResponse()

    def ConsultarProdutoPreco(self, request, context):
        preco_max = request.preco_max
        produtos = [
            produtos_pb2.Produto(nome=nome, preco=dados["preco"], quantidade=dados["quantidade"])
            for nome, dados in catalogo_produtos.items()
            if dados["preco"] <= preco_max
        ]
        return produtos_pb2.ListaProdutos(produtos=produtos)

    def AtualizarEstoque(self, request, context):
        nome = request.nome
        quantidade = request.quantidade
        if nome in catalogo_produtos:
            catalogo_produtos[nome]["quantidade"] += quantidade
            return produtos_pb2.AtualizarResponse(mensagem=f"Estoque de '{nome}' atualizado com sucesso.")
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details(f"Produto '{nome}' não encontrado.")
        return produtos_pb2.AtualizarResponse()

def servidor():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    produtos_pb2_grpc.add_ProdutoServiceServicer_to_server(ProdutoService(), server)

    port = server.add_insecure_port("[::]:0")  # escolhe uma porta dinâmica
    print(f"Servidor gRPC em execução na porta {port}...")
    server.start()
    with open("server_port.txt", "w") as file:
        file.write(str(port))  # salva a porta para o cliente usar
    server.wait_for_termination()

if __name__ == "__main__":
    servidor()
