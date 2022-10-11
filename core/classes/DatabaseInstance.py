from flet import Container,Row,Text,ElevatedButton,Column,colors
from core.classes.TableInstance import TableInstance
class DatabaseInstance:
    data = {}


    def createtableView(self):
        print(f"let's create a new table in database {self.name}")
        return []
        
    def tablelistView(self,master):
        list = []
        for tb in self.gettables():
            tbcontainer = Container(bgcolor=colors.WHITE)
            tbcolumn = Column()
            tbrow = Row()
            tbrow.width = master.view.width
            tbnamecontainer = Container(padding=2)
            tbnamecontainer.width = tbrow.width
            tbname = Text(value=tb.name)
            tbactions = Row()
            rename_database_button = ElevatedButton(text='rename')
            drop_database_button = ElevatedButton(text='drop')
            list_fields_button = ElevatedButton(text='fields')
            drop_database_button.bgcolor = colors.RED_200
            tbactions.controls = [rename_database_button,drop_database_button,list_fields_button] 
            tbnamecontainer.content=tbname
            tbrow.controls = [tbnamecontainer]
            tbcolumn.controls.append(tbrow)
            tbcolumn.controls.append(tbactions)
            tbcontainer.content = tbcolumn
            list.append(tbcontainer)
        return list

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
        return f"#>{self.name}"

    def __init__(self,serverinstance,raw):
        self.server = serverinstance
        self.name =  raw[0]
        self.setdata()