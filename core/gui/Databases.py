from flet import Text, TextField, ElevatedButton, Column, Row, Container, colors
from core.classes.ServerInstance import ServerInstance




class DatabasesView:
    server = None

    def __init__(self,master,server=None):
        self.master = master
        self.server = server
        self.build_components()
        
    def build_components(self):
        self.container = Container(bgcolor=colors.BLUE_200)
        self.databases_container = Column()
        self.databases_container.controls.append(Text(value='texte'))
        self.container.content =self.databases_container

    def update_form(self):
        self.form.update()

    def append_to(self,target):
        self.container.width = target.width
        self.databases_container.width = target.width
        target.controls.append(self.container)