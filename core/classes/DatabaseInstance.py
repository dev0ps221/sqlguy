from flet import Container,Row,Text,ElevatedButton,Column,colors,TextField,Dropdown,dropdown
from core.classes.TableInstance import TableInstance
class DatabaseInstance:
    data = {}


    def createtableView(self,master):
        createtablecontainer = Container()
        createtablecolumn = Column()

        fieldscontainer = Container()
        fieldscontainer.width = master.view.width
        fieldscolumn = Column()
        fieldslist = Column()
        fieldslabel = Text(value='Fields')
        addfieldbutton = ElevatedButton(text='add')

        keyscontainer = Container()
        keyscontainer.width = master.view.width
        keyscolumn = Column()
        keysdata = Row()
        keyslabel = Text(value='Keys')

        primarykeyscontainer = Container()
        primarykeyscolumn = Column()
        primarykeyslist = Column()
        primarykeyslabel = Text(value='primary')
        addprimarykeybutton = ElevatedButton(text='add')

        foreignkeyscontainer = Container()
        foreignkeyscolumn = Column()
        foreignkeyslabel = Text(value='foreign')
        foreignkeyslist = Column()
        addforeignkeybutton = ElevatedButton(text='add')
        
        uniquekeyscontainer = Container()
        uniquekeyscolumn = Column()
        uniquekeyslabel = Text(value='unique')
        adduniquekeybutton = ElevatedButton(text='add')

        def addfield(event):
            fieldcontainer = Container()
            fieldrow = Row()
            fieldname = TextField(label='name')
            fieldtype = Dropdown(label='type')
            fieldnull = Dropdown(label='null')
            fieldoptions = TextField(label='options')
            fieldrow.controls = [fieldname,fieldtype,fieldnull,fieldoptions]
            fieldcontainer.content = fieldrow
            fieldslist.width = master.view.width
            fieldrow.width = master.view.width
            for control in fieldrow.controls:
                control.width = int((fieldrow.width)/len(fieldrow.controls))-10
            fieldslist.controls.append(fieldcontainer)
            fieldslist.update()

        def addprimarykeyfield(event):
            primarykeycontainer = Container()
            primarykeyselect = Dropdown(label='select a field')
            primarykeycontainer.content = primarykeyselect
            primarykeyslist.width = master.view.width
            primarykeyslist.controls = [primarykeycontainer]
            primarykeyslist.update()
        
        def adduniquekeyfield(event):
            uniquekeycontainer = Container()
            uniquekeyselect = Dropdown(label='select a field')
            uniquekeycontainer.content = uniquekeyselect
            uniquekeyslist.width = master.view.width
            uniquekeyslist.controls = [uniquekeycontainer]
            uniquekeyslist.update()

        def addforeignkeyfield(event):
            foreignkeycontainer = Container()
            foreignkeyselect = Dropdown(label='select a field')
            foreignkeycontainer.content = foreignkeyselect
            foreignkeyslist.width = master.view.width
            foreignkeyslist.controls = [foreignkeycontainer]
            foreignkeyslist.update()


        addfieldbutton.on_click = addfield
        addprimarykeybutton.on_click = addprimarykeyfield
        addforeignkeybutton.on_click = addforeignkeyfield
        adduniquekeybutton.on_click = adduniquekeyfield

        fieldscolumn.controls = [fieldslabel,fieldslist,addfieldbutton]
        fieldscontainer.content = fieldscolumn
        
        primarykeyscontainer.content = primarykeyscolumn
        primarykeyscolumn.controls = [primarykeyslabel,primarykeyslist,addprimarykeybutton]

        foreignkeyscontainer.content = foreignkeyscolumn
        foreignkeyscolumn.controls = [foreignkeyslabel,foreignkeyslist,addforeignkeybutton]

        uniquekeyscontainer.content = uniquekeyscolumn
        uniquekeyscolumn.controls = [uniquekeyslabel,adduniquekeybutton]

        keysdata.controls = [primarykeyscontainer,uniquekeyscontainer,foreignkeyscontainer]
        keyscolumn.controls = [keyslabel,keysdata]
        keyscontainer.content = keyscolumn

        createtablecolumn.controls = [fieldscontainer,keyscontainer]
        createtablecontainer.content = createtablecolumn

        return [createtablecontainer]
        
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