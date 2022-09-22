import mysql.connector

class ServerInstance:
    host = None
    user = None
    pwd = None
    connected = False
    dbinstance = None
    cursor = None
    def connect(self):
        self.dbinstance = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.pwd
        )
    def getcursor(self):
        if self.cursor is None:
    def delcursor(self):
        self.cursor = None
        print(self.dbinstance)

    def __init__(self, host, user, pwd):
        self.host = host
        self.user = user
        self.pwd  = pwd
    
server = ServerInstance('','root','')
server.connect()