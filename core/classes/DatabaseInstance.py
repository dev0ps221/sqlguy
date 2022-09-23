class DatabaseInstance:

    def query(self,query):
        return self.server.executereq(query)

    def use(self):
        self.query(f"use {self.name}")

    def process_databases(self,tables):
        tbs = []
        for db in tables:
            tbs.append(DatabaseInstance(self,db))
        return tbs

    def setdata(self):
        self.data = {'databases':self.process_databases(self.executereq('show databases'))}

    def __init__(self,serverinstance,raw):
        self.server = serverinstance
        self.name,self.rawerror = raw

    print(raw)  