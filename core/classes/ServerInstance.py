import mysql.connector

class ServerInstance:
    host = None
    user = None
    pwd = None
    connected = False

    def connect(self):
        

    def __init__(self, host, user, pwd):
        self.host = host
        self.user = user
        self.pwd  = pwd
    