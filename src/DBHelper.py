import sqlite3
from sqlite3 import Error
import GrpcExampleService_pb2

""" constants and database queries """
sql_strings = {
    "check": "SELECT name FROM sqlite_master WHERE type='table' AND name='client'",
    "database_addr": "../database/mydatabase.db",
    "create_client": "CREATE TABLE client(id INTEGER PRIMARY KEY AUTOINCREMENT, login text UNIQUE, email text, city text)",
    "add_client": 'INSERT INTO client(login, email, city) VALUES(\'{0}\',\'{1}\',\'{2}\')',
    "get_clients": "SELECT * FROM client",
    "get_client_by_login": "SELECT * FROM client WHERE login = \'{0}\'",
    "modify_client_by_id": "UPDATE client SET email = coalesce({1}, email), city = coalesce({2}, city)  WHERE id = {0}",
}

class DBHelper:
    def __init__(self):
        try:
            con = sqlite3.connect(sql_strings["database_addr"])
            cursor = con.cursor()
            result = cursor.execute(sql_strings["check"])
            if len(result.fetchall()) == 0:
                # need to initialize the database structure
                self.init_db_structure(cursor, con)
            con.close()
        except Error:
            print(Error.args[0])

    def init_db_structure(self, cursor, con):
        cursor.execute(sql_strings["create_client"])
        con.commit()

    def add_clients(self, info):
        try:
            if len(info) == 0:
                return GrpcExampleService_pb2.addClientReply(
                    response_error=GrpcExampleService_pb2.ResponseError(
                        message='Empty request!',
                        response_error_code=GrpcExampleService_pb2.ResponseErrorCode.RESPONSE_BAD_REQUEST))
            con = sqlite3.connect(sql_strings["database_addr"])
            cursor = con.cursor()
            for client in info:
                cursor.execute(sql_strings["add_client"].format(
                    client.login, client.email, client.city))
            con.commit()
            con.close()
            return GrpcExampleService_pb2.addClientReply(
                response_ok=GrpcExampleService_pb2.ResponseOk())
        except Error as err:
            if err.args[0].startswith("UNIQUE"):
                return GrpcExampleService_pb2.addClientReply(
                    response_error=GrpcExampleService_pb2.ResponseError(
                        message='Login {0} already exists!'.format(
                            client.login),
                        response_error_code=GrpcExampleService_pb2.ResponseErrorCode.RESPONSE_BAD_REQUEST))
            else:
                return GrpcExampleService_pb2.addClientReply(
                    response_error=GrpcExampleService_pb2.ResponseError(
                        response_error_code=GrpcExampleService_pb2.ResponseErrorCode.RESPONSE_ERROR,
                        message=str(err)))

    def get_clients(self):
        try:
            con = sqlite3.connect(sql_strings["database_addr"])
            cursor = con.cursor()
            result = cursor.execute(sql_strings["get_clients"])
            clientsResp = GrpcExampleService_pb2.ClientsInfoResponse()
            for row in result:
                clientInfo = clientsResp.clients.add()
                clientInfo.id = row[0]
                clientInfo.login = row[1]
                clientInfo.email = row[2]
                clientInfo.city = row[3]

            con.close()
            return GrpcExampleService_pb2.GetClientsReply(
                response_clients=clientsResp) 
        except Error as err:
            GrpcExampleService_pb2.GetClientsReply(
                    response_error=GrpcExampleService_pb2.ResponseError(
                        response_error_code=GrpcExampleService_pb2.ResponseErrorCode.RESPONSE_ERROR, 
                        message=str(err)))

    def get_client_by_login(self, login):
        try:
            con = sqlite3.connect(sql_strings["database_addr"])
            cursor = con.cursor()
            result = cursor.execute(
                sql_strings["get_client_by_login"].format(login))
            clientsResp = GrpcExampleService_pb2.ClientsInfoResponse()
            for row in result:
                clientInfo = clientsResp.clients.add()
                clientInfo.id = row[0]
                clientInfo.login = row[1]
                clientInfo.email = row[2]
                clientInfo.city = row[3]

            con.close()
            return GrpcExampleService_pb2.GetClientsReply(
                response_clients=clientsResp) 
        except Error as err:
            GrpcExampleService_pb2.GetClientsReply(
                    response_error=GrpcExampleService_pb2.ResponseError(
                        response_error_code=GrpcExampleService_pb2.ResponseErrorCode.RESPONSE_ERROR, 
                        message=str(err)))
            
    def modify_client_by_id(self, id, email, city):
        try:
            con = sqlite3.connect(sql_strings["database_addr"])
            cursor = con.cursor()
            result = cursor.execute(
                sql_strings["modify_client_by_id"].format(id, email, city))
            con.commit()
            con.close()
            return GrpcExampleService_pb2.ModifyClientByIdReply(
                response_ok=GrpcExampleService_pb2.ResponseOk())
        except Error as err:
            GrpcExampleService_pb2.GetClientsReply(
                    response_error=GrpcExampleService_pb2.ResponseError(
                        response_error_code=GrpcExampleService_pb2.ResponseErrorCode.RESPONSE_ERROR, 
                        message=str(err)))
