from flet import Text, TextField, ElevatedButton, Column, Row, Container, colors





class ServersView:

    servers = []

    def __init__(self,master,servers=[]):
        self.master = master
        self.servers = servers
        self.update_servers(self.servers)
        self.build_components()

    def do_logout(self):
        pass

    def build_components(self):
        self.container = Container()
        self.servers_container = Container()
        self.servers_view = Row()
        self.servers_container.controls = self.getservers()
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