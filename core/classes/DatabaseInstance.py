from core.classes.TableInstance import TableInstance
class DatabaseInstance:
    data = {}
    def query(self,query):
        return self.server.executereq(query)

    def use(self):
        self.query(f"use {self.name}")

    def process_tables(self,tables):
        tbs = []
        for tb in tables:
            tbs.append(TableInstance(self,tb))
        return tbs

    def gettables(self):
        return  self.data['tables'] if 'tables' in  self.data else [] 

    def setdata(self):
        self.use()
        self.data = {'tables':self.process_tables(self.query('show tables'))}

    def __repr__(self):
        return f"{self.name}:{self.gettables()}"

    def __init__(self,serverinstance,raw):
        self.server = serverinstance
        self.name =  raw[0]
        self.setdata()