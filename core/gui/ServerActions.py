from flet import Text, TextField, ElevatedButton, Column, Row, Container, colors
from core.classes.ServerInstance import ServerInstance




class ServerActionsView:
    server = None
    selected_database = None
    selected_view = None
    databases_container_label=Text(value='DATABASES')
    databases = Row(scroll='adaptive')
    serveractions = Row(scroll='adaptive')
    databases_container = Column()
    container = Container(bgcolor=colors.BLUE_200)
    listdatabasebutton = ElevatedButton(text='list',on_click=lambda x :self.on_click(x,x.control.text))
    def __init__(self,master,server=None):
        self.master = master
        self.server = server
        
    def update(self):
        self.container.clean()
        self.build_components()
        self.container.update()

    def select_database(self,name):
        for database in self.getdatabases():
            if database.name == name:
                self.selected_database = database
        self.update()

    def select_view(self,view):
        self.selected_view = view
        self.update()

    def getdatabases(self):
        return self.master.actual_server.getdatabases() if self.master.actual_server else []

    def build_components_old(self):
        self.databases_container.controls = []
        self.databases.controls = []
        for database in self.getdatabases():
            def on_click(x):
                self.select_database(x.control.text)
            databasebutton = ElevatedButton(text=database.name,on_click=on_click) 
            if self.selected_database is not None and self.selected_database.name == database.name:
                print('bileu ',self.selected_database.name)
                databasebutton.bgcolor = colors.GREEN_400
            self.databases.controls.append(databasebutton)
        self.databases_container.controls.append(self.databases_container_label)
        self.databases_container.controls.append(self.databases)
        self.container.content = self.databases_container

    def on_select_view(self,view):
        self.select_view(view)
            

    def build_components(self):
        self.databases_container.controls = []
       
        if self.master.actual_server:
            self.serveractions.controls = []
            if self.selected_view is None :
                self.select_view('list')
            
            self.serveractions.controls.append(self.listdatabasebutton)
            self.databases_container.controls.append(self.databases_container_label)
            self.databases_container.controls.append(self.serveractions)
        self.container.content = self.databases_container
        
    def update_form(self):
        self.form.update()

    def append_to(self,target):
        target.controls = []
        self.container.width = target.width
        self.databases_container.width = target.width
        self.container.height = target.height
        self.databases_container.height = target.height
        target.controls.append(self.container)