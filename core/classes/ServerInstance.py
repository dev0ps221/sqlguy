import mysql.connector
from flet import Text,Column,ElevatedButton,Container,Row,TextField
from core.classes.DatabaseInstance import DatabaseInstance
class ServerInstance:
    host = None
    user = None
    pwd = None
    connected = False
    dbinstance = None
    cursor = None
    data = {}

    def createdatabaseView(self,master):
        createdatabasecontainer = Container()
        databasenamecontainer = Container()
        databasenamecolumn = Column()
        databasename = TextField(label='the new database\'s name')
        statustextrow = Row()
        statustext = Text()
        validatecreatedatabase = ElevatedButton(text='create')
        databasenamecontainer.content = databasename
        statustextrow.controls = [statustext]
        databasenamecolumn.controls = [databasenamecontainer,validatecreatedatabase,statustextrow]
        createdatabasecontainer.content = databasenamecolumn
        validatecreatedatabase.on_click = lambda event : self.process_create_database(databasename,validatecreatedatabase,statustextrow,statustext,master)
        return [createdatabasecontainer] 

    def create_database(self,dbname):
        req = f"CREATE database {dbname}"
        print(self.executereq(req))
        req = f"show databases like '{dbname}'"
        doesexist = self.executereq(req)
        exists,error = None,None
        if len(doesexist):
            match = doesexist[0]
            exists,error = (match[0],match[1] if len(match)>1 else None)
        if error:
            print("ERROR WHEN ATTEMPTING TO CREATE DATABASE")
            print(f"\t-{error}")
        return exists


    def process_create_database(self,name,button,statustextrow,statustext,master):
        if name.value:
            statustext.value = f'{"SUCCESS" if self.create_database(name.value) else "FAILED"} CREATING DATABASE {name.value}'
            statustext.update()
            statusaction = ElevatedButton(text=f'select database {name.value}',on_click=lambda event:master.ServerActions.select_database(name.value))
            statustextrow.controls = [statustext,statusaction]
            statustextrow.update()

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


    def getdatabases(self):
        return  self.data['databases'] if 'databases' in  self.data else [] 

    def executereq(self,req):
        self.getcursor().execute(req) if self.getcursor() else None
        res = self.retrieve_results()
        self.setcursor()
        return res
    
    def delcursor(self):
        self.cursor = None

    def process_databases(self,deebees):
        dbs = []
        for db in deebees:
            dbs.append(DatabaseInstance(self,db))
        return dbs

    def setdata(self):
        self.data = {'databases':self.process_databases(self.executereq('show databases'))}

    def __repr__(self):
        return f"{self.user}@{self.host}"

    def __fidrepr__(self):
        return f"{self.user}:{self.pwd}@{self.host}"

    def start(self):
        self.connect()
        self.setdata()
        return self.cursor

    def __init__(self, host, user, pwd):
        self.host = host
        self.user = user
        self.pwd  = pwd
    