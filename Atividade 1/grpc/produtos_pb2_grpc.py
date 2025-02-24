# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import produtos_pb2 as produtos__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in produtos_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ProdutoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListarProdutos = channel.unary_unary(
                '/ProdutoService/ListarProdutos',
                request_serializer=produtos__pb2.Empty.SerializeToString,
                response_deserializer=produtos__pb2.ListaProdutos.FromString,
                _registered_method=True)
        self.ConsultarProdutoNome = channel.unary_unary(
                '/ProdutoService/ConsultarProdutoNome',
                request_serializer=produtos__pb2.ProdutoRequest.SerializeToString,
                response_deserializer=produtos__pb2.ProdutoResponse.FromString,
                _registered_method=True)
        self.ConsultarProdutoPreco = channel.unary_unary(
                '/ProdutoService/ConsultarProdutoPreco',
                request_serializer=produtos__pb2.PrecoRequest.SerializeToString,
                response_deserializer=produtos__pb2.ListaProdutos.FromString,
                _registered_method=True)
        self.AtualizarEstoque = channel.unary_unary(
                '/ProdutoService/AtualizarEstoque',
                request_serializer=produtos__pb2.AtualizarRequest.SerializeToString,
                response_deserializer=produtos__pb2.AtualizarResponse.FromString,
                _registered_method=True)


class ProdutoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListarProdutos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConsultarProdutoNome(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConsultarProdutoPreco(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AtualizarEstoque(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProdutoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListarProdutos': grpc.unary_unary_rpc_method_handler(
                    servicer.ListarProdutos,
                    request_deserializer=produtos__pb2.Empty.FromString,
                    response_serializer=produtos__pb2.ListaProdutos.SerializeToString,
            ),
            'ConsultarProdutoNome': grpc.unary_unary_rpc_method_handler(
                    servicer.ConsultarProdutoNome,
                    request_deserializer=produtos__pb2.ProdutoRequest.FromString,
                    response_serializer=produtos__pb2.ProdutoResponse.SerializeToString,
            ),
            'ConsultarProdutoPreco': grpc.unary_unary_rpc_method_handler(
                    servicer.ConsultarProdutoPreco,
                    request_deserializer=produtos__pb2.PrecoRequest.FromString,
                    response_serializer=produtos__pb2.ListaProdutos.SerializeToString,
            ),
            'AtualizarEstoque': grpc.unary_unary_rpc_method_handler(
                    servicer.AtualizarEstoque,
                    request_deserializer=produtos__pb2.AtualizarRequest.FromString,
                    response_serializer=produtos__pb2.AtualizarResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProdutoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ProdutoService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ProdutoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListarProdutos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ProdutoService/ListarProdutos',
            produtos__pb2.Empty.SerializeToString,
            produtos__pb2.ListaProdutos.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ConsultarProdutoNome(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ProdutoService/ConsultarProdutoNome',
            produtos__pb2.ProdutoRequest.SerializeToString,
            produtos__pb2.ProdutoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ConsultarProdutoPreco(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ProdutoService/ConsultarProdutoPreco',
            produtos__pb2.PrecoRequest.SerializeToString,
            produtos__pb2.ListaProdutos.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AtualizarEstoque(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ProdutoService/AtualizarEstoque',
            produtos__pb2.AtualizarRequest.SerializeToString,
            produtos__pb2.AtualizarResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
