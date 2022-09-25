from core.gui.Forms import ServerForm
from flet import Text, TextField, ElevatedButton, Column, Row, Container, colors





class ServersView:

    servers = []

    def add_server(self,event,fields):
        [print(field.elem.elem) for field in fields]

    def __init__(self,master,servers=[]):
        self.master = master
        self.servers = servers
        self.add_server_form = ServerForm(OnSubmit=self.add_server)
        self.update_servers(self.servers)
        self.build_components()

    def do_logout(self):
        pass

    def build_components(self):
        self.container = Container()
        self.servers_container = Column()
        self.servers_view = Row()
        self.add_server_form.formview.append_to(self.servers_container)
        for server in self.getservers():
            self.servers_container.controls.append(server)
        self.container.content = self.servers_container

    def getservers(self):
        return self.servers

    def update_servers(self,servers):
        lst = []
        self.servers = servers
        for server in servers:
            serverButton = ElevatedButton(text=server.host)
            lst.append(serverButton)
        self.servers = lst
        return self.getservers()

    def update(self):
        self.server_view.update()

    def append_to(self,target):
        self.container.width = target.width
        self.servers_container.width = target.width
        target.controls.append(self.container)