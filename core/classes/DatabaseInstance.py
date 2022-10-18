from flet import Container,Row,Text,ElevatedButton,Column,colors,TextField,Dropdown,dropdown
from core.classes.TableInstance import TableInstance
class DatabaseInstance:
    data = {}


    def createtableView(self,master):
        global removefieldbuttons 
        removefieldbuttons = []
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
        primarykeyscontainer.width = int(master.view.width/3)-10
        primarykeyscolumn = Column()
        primarykeyslist = Column()
        primarykeyslabel = Text(value='primary')
        addprimarykeybutton = ElevatedButton(text='add')

        foreignkeyscontainer = Container()
        foreignkeyscontainer.width = int(master.view.width/3)-10
        foreignkeyscolumn = Column()
        foreignkeyslabel = Text(value='foreign')
        foreignkeyslist = Column()
        addforeignkeybutton = ElevatedButton(text='add')
        
        uniquekeyscontainer = Container()
        uniquekeyscontainer.width = int(master.view.width/3)-10
        uniquekeyscolumn = Column()
        uniquekeyslabel = Text(value='unique')
        uniquekeyslist = Column()
        adduniquekeybutton = ElevatedButton(text='add')

        def create_table_data():
            True
        def create_table_keys():
            True
        def addfield(event):
            fieldcontainer = Container()
            fieldslist.controls.append(fieldcontainer)
            containeridx = len(fieldslist.controls)-1
            fieldrow = Row()
            fieldname = TextField(label='name')
            fieldtype = Dropdown(label='type')
            fieldnull = Dropdown(label='null')
            fieldoptions = TextField(label='options')
            fieldremove = ElevatedButton(text='remove',bgcolor=colors.RED_400)
            removefieldbuttons.append(fieldremove)
            fieldrow.controls = [fieldname,fieldtype,fieldnull,fieldoptions,fieldremove]
            fieldcontainer.content = fieldrow
            fieldslist.width = master.view.width
            fieldrow.width = master.view.width
            
            for control in fieldrow.controls:
                control.width = int((fieldrow.width)/len(fieldrow.controls))-10

            def delfield(x,containeridx):
                global removefieldbuttons
                controls = []
                for idx,control in enumerate(fieldslist.controls):
                    if containeridx != idx: controls.append(control)
                fieldslist.controls = controls
                buttons = []  
                for idx,button in enumerate(removefieldbuttons):
                    if containeridx != idx: buttons.append(button)
                removefieldbuttons = buttons
                for idx,button in enumerate(removefieldbuttons):
                    button.on_click = lambda x:delfield(x,idx)        
                
                fieldslist.update()

            fieldremove.on_click = lambda x:delfield(x,containeridx)
            fieldslist.update()

        def addprimarykeyfield(event):
            primarykeycontainer = Container()
            primarykeyselect = Dropdown(label='select a field')
            primarykeyselect.width = int(master.view.width/3)
            primarykeycontainer.content = primarykeyselect
            primarykeyslist.width = int(master.view.width/3)
            primarykeyslist.controls = [primarykeycontainer]
            primarykeyslist.update()
            keysdata.controls = [primarykeyscontainer,uniquekeyscontainer,foreignkeyscontainer]
            

        def adduniquekeyfield(event):
            uniquekeycontainer = Container()
            uniquekeyselect = Dropdown(label='select a field')
            uniquekeyselect.width = int(master.view.width/3)
            uniquekeycontainer.content = uniquekeyselect
            uniquekeyslist.width = int(master.view.width/3)
            uniquekeyslist.controls = [uniquekeycontainer]
            uniquekeyslist.update()
            keysdata.controls = [primarykeyscontainer,uniquekeyscontainer,foreignkeyscontainer]
            

        def addforeignkeyfield(event):
            foreignkeycontainer = Container()
            foreignkeyselect = Dropdown(label='select a field')
            foreignkeyselect.width = int(master.view.width/3)
            foreignkeycontainer.content = foreignkeyselect
            foreignkeyslist.width = int(master.view.width/3)
            foreignkeyslist.controls = [foreignkeycontainer]
            foreignkeyslist.update()
            keysdata.controls = [primarykeyscontainer,uniquekeyscontainer,foreignkeyscontainer]
            


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
        uniquekeyscolumn.controls = [uniquekeyslabel,uniquekeyslist,adduniquekeybutton]

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