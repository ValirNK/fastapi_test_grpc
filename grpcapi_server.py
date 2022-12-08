import json
from concurrent import futures
import logging
import grpc
import grpcapi_pb2
import grpcapi_pb2_grpc
from pysondb import db
import argparse
from logging import basicConfig, DEBUG, info, error, debug, warning
basicConfig(filename="logs.log", level=DEBUG)

db_name = 'db.json'
parser = argparse.ArgumentParser()
parser.add_argument('-db', '--json_database', default='db.json')
namespace = parser.parse_args()

class SaveDocServicer(grpcapi_pb2_grpc.SaverServicer):
  def __init__(self):
    try:
      self.json_doc = json.loads(open(namespace.json_database, 'r', encoding='utf-8').read())
    except (Exception) as ex:
      logging.warning(ex)
      self.json_doc = None
    self.db = db.getDb('server_db.json')

  def SaveDoc(self, request, context):
    print('SaveDoc method')
    if not self.json_doc is None:
      many_docs = []
      for json_obj in self.json_doc:
        retrieve = self.db.getByQuery(query={"article_id": json_obj["article_id"]})
        if retrieve == []:
          many_docs.append(json_obj)
        else:
          logging.info(f'Record with article_id {json_obj["article_id"]} exist in database')
          pass
      self.db.addMany(many_docs)
      logging.info('Records Saved to database')
    return grpcapi_pb2.DocObj()


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  grpcapi_pb2_grpc.add_SaverServicer_to_server(
    SaveDocServicer(), server)
  port = 50051
  if namespace.json_database:
    logging.info(f'Server starts on {port} port')
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info(f'Server starts on {port} port')
    logging.info(f'Selected json database: {namespace.json_database}')
    server.wait_for_termination()
  else:
    logging.info('Missing argument json_file')


if __name__ == '__main__':
  logging.basicConfig()
  serve()
