# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpcapi_pb2 as grpcapi__pb2


class SaverStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SaveDoc = channel.unary_unary(
                '/fastapi.Saver/SaveDoc',
                request_serializer=grpcapi__pb2.DocObj.SerializeToString,
                response_deserializer=grpcapi__pb2.DocObj.FromString,
                )


class SaverServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SaveDoc(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SaverServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SaveDoc': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveDoc,
                    request_deserializer=grpcapi__pb2.DocObj.FromString,
                    response_serializer=grpcapi__pb2.DocObj.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fastapi.Saver', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Saver(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SaveDoc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fastapi.Saver/SaveDoc',
            grpcapi__pb2.DocObj.SerializeToString,
            grpcapi__pb2.DocObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
