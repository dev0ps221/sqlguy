class DatabaseInstance:
    data = {}
    def query(self,query):
        return self.server.executereq(query)

    def use(self):
        self.query(f"use {self.name}")

    def process_tables(self,tables):
        tbs = []
        for tb in tables:
            tbs.append(DatabaseInstance(self,tb))
        return tbs

    def gettables(self):
        return  self.data['tables'] if 'tables' in  self.data else [] 

    def setdata(self):
        self.data = {'tables':self.process_tables(self.query('show tables'))}

    def __init__(self,serverinstance,raw):
        self.server = serverinstance
        self.name,self.rawerror = raw
        self.setdata()