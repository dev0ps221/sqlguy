from flet import Text, TextField, ElevatedButton, Column, Row, Container, colors
from core.classes.ServerInstance import ServerInstance




class DatabasesView:
    server = None
    databases_container = Column()
    container = Container(bgcolor=colors.BLUE_200)

    def __init__(self,master,server=None):
        self.master = master
        self.server = server
        self.build_components()
        
    def update(self):
        self.build_components()
        self.container.update()

    def build_components(self):
        if self.master.actual_server:
            self.databases_container.controls = []
            for database in self.master.actual_server.getdatabases():
                databasebutton = ElevatedButton(text=database.name) 
                self.databases_container.controls.append(databasebutton)
        self.container.content = self.databases_container

    def update_form(self):
        self.form.update()

    def append_to(self,target):
        self.container.width = target.width
        self.databases_container.width = target.width
        target.controls.append(self.container)