from __future__ import print_function
import logging
import grpc
import grpcapi_pb2
import grpcapi_pb2_grpc
from datetime import datetime

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpcapi_pb2_grpc.SaverStub(channel)
        print('Client ready')
        response = stub.SaveDoc(grpcapi_pb2.DocObj(
          article_id=35335,
          text="Welcome Text",
          title="Welcome Title",
          date=str(datetime.now()),
          lang=grpcapi_pb2.EN,
          locations=[grpcapi_pb2.DocObj.Location(lat=2.5464, lon=8.6353)],
          semantic_vector=[grpcapi_pb2.DocObj.Vector(value=i) for i in range(111,999)],
          keywords=[grpcapi_pb2.DocObj.Keyword(name=keyword) for keyword in ['k1','k2','k3']],
          entities=[grpcapi_pb2.DocObj.Entity(name=entity) for entity in ['ent1','ent2','ent3']],
          themes=[grpcapi_pb2.DocObj.Theme(name=theme) for theme in ['theme1','theme2']],
          _class=[grpcapi_pb2.DocObj.Class(name=cl) for cl in ['item1','item2']]
        ))


if __name__ == '__main__':
    logging.basicConfig()
    run()
