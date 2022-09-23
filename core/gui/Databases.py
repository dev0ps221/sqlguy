from flet import Text, TextField, ElevatedButton, Column, Row, Container, colors
from core.classes.ServerInstance import ServerInstance




class DatabasesView:
    server = None

    def __init__(self,master,server=None):
        self.master = master
        self.server = server
        self.build_components()
        
    def build_components(self):
        self.container = Container()
        self.databases_container = Container()
        self.container.content =self.databases_container

    def update_form(self):
        self.form.update()

    def append_to(self,target):
        target.controls.append(self.container)