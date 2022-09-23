from flet import Text, TextField, ElevatedButton, Column, Row, Container, colors





class ServersView:

    def __init__(self,master):
        self.master = master

    def do_logout(self):
        pass

    def build_components(self):
        self.container = Container()
        self.servers_container = Container()
        self.servers_view = Row()
        self.servers_container.controls = self.servers
        self.container.content = self.servers_container

    def update_servers(self):
        self.server_view.update()

    def append_to(self,target):
        self.target.add(self.container)