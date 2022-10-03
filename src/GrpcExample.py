# Autor Mikhail Petrov
# 02.10.2022

"""gRPC's Python Example services."""
import grpc
import concurrent.futures as futures
import GrpcExampleService_pb2_grpc
import DBHelper

""" A python class that implements .proto file's methods """
class GrpcExampleService(GrpcExampleService_pb2_grpc.GrpcExampleService):
  dbhelper = 0
  """ Gets all the information about our customers """
  def AddClient(self, request, context):
    return self.dbhelper.add_clients(request.clientsinfo)
  """ Gets all the information about our customers """
  def GetClients(self, request, context):
    return self.dbhelper.get_clients()
  """ Gets all the information about our customer by login """
  def GetClientByLogin(self, request, context):
    return self.dbhelper.get_client_by_login(request.login)

""" Inizialize and start our gRPC's service """
def service():
  GrpcExampleService.dbhelper = DBHelper.DBHelper()
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  GrpcExampleService_pb2_grpc.add_GrpcExampleServiceServicer_to_server(GrpcExampleService(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()

if __name__ == '__main__':
    print('GrpcExample service start')
    service()