import mysql.connector

class ServerInstance:
    host = None
    user = None
    pwd = None
    connected = False
    dbinstance = None
    cursor = None
    data = {}

    def connect(self):
        self.dbinstance = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.pwd
        )
        return self.getcursor()

    def setcursor(self):
        self.cursor = self.dbinstance.cursor() if self.dbinstance is not None else self.cursor
        return self.gotcursor()

    def retrieve_results(self):
        res = []
        for r in self.cursor:
            res.append(r)
        return res

    def getcursor(self):
        if self.cursor is None:
            self.setcursor()
        return self.cursor

    def gotcursor(self):
        return self.cursor is not None


    def executereq(self,req):
        self.getcursor().execute(req) if self.getcursor() else None
        res = self.retrieve_results() 
        self.setcursor()
        return res
    
    def delcursor(self):
        self.cursor = None

    def process_databases(self,dbs):
        dbs = []
        for db in dbs:
            
        return dbs

    def setdata(self):
        self.data = {'databases':self.process_databases(self.executereq('show databases'))}

    def __init__(self, host, user, pwd):
        self.host = host
        self.user = user
        self.pwd  = pwd
        self.connect()
        self.setdata()
    
server = ServerInstance('','root','')