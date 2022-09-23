class TableInstance:

    def query(self,query):
        self.database.query(query)

    def process_fields(self,fields):
        flds = []
        if fields:
            for fld in fields:
                flds.append(DatabaseInstance(self,fld))
        return flds

    def getfields(self):
        return  self.data['fields'] if 'fields' in  self.data else [] 

    def setdata(self):
        self.data = {'fields':self.process_fields(self.query(f' select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME= "{self.name}"'))}

    def __repr__(self):
        return f"{self.name}:{self.getfields()}"

    def __init__(self,database,raw):
        self.database = database
        self.name = raw[0] 
        self.setdata()