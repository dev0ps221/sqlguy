from flet import Text, TextField, ElevatedButton, Column, Row, Container, colors
from core.classes.ServerInstance import ServerInstance




class DatabasesView:
    server = None
    selected_database = None
    selected_view = None
    databases_container_label=Text(value='DATABASES')
    databases = Row(scroll='adaptive')
    databasesactions = Row(scroll='adaptive')
    databases_container = Column()
    container = Container(bgcolor=colors.BLUE_200)

    def __init__(self,master,server=None):
        self.master = master
        self.server = server
        self.build_components()
        
    def update(self):
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

    def build_components(self):
        self.databases_container.controls = []
        self.databasesactions.controls = []
        def on_click(x):
            self.select_view(x.control.text)
        print(self.selected_view)
        listdatabasebutton = ElevatedButton(text='list',on_click=on_click) 
        self.databases_container.controls.append(self.databases_container_label)
        self.databases_container.controls.append(self.databasesactions)
        self.container.content = self.databases_container

    def update_form(self):
        self.form.update()

    def append_to(self,target):
        self.container.width = target.width
        self.databases_container.width = target.width
        self.container.height = target.height
        self.databases_container.height = target.height
        target.controls.append(self.container)