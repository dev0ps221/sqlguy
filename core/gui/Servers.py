from core.classes.ServerInstance import ServerInstance
from core.gui.Forms import ServerForm
from flet import Text, TextField, ElevatedButton, Column, Row, Container, colors, alignment





class ServersView:

    container = Container()
    servers_container = Column(scroll='adaptive')
    servers = []
    serversdata = []

    def add_server(self,event,fields):
        data = {}
        for field in fields:
            if hasattr(field,'name'):
                data[field.name] = field.elem.elem.value
        if 'host' in data and 'username' in data and 'password' in data:
            self.serversdata.append(ServerInstance(data['host'],data['username'],data['password']))
            self.update_servers()
            self.build_components()
            self.servers_container.update()

    def __init__(self,master,servers=[]):
        self.master = master
        self.servers = servers
        self.add_server_form = ServerForm(OnSubmit=self.add_server)
        self.update_servers(self.servers)
        self.build_components()
    def do_logout(self):
        pass

    def build_components(self):
        self.servers_container.controls = []
        self.servers_container.width = int(self.master.wwidth()*(30/100))
        addserverlabeltext = Text(value='ADD A SERVER',bgcolor=colors.WHITE)
        addserverlabeltext.width = self.add_server_form.
        addserverlabeltext.alignment=alignment.center
        self.servers_container.controls.append(addserverlabeltext)
        self.add_server_form.formview.append_to(self.servers_container)
        for server in self.getservers():
            self.servers_container.controls.append(server)
        self.container.content = self.servers_container

    def getservers(self):
        return self.servers

    def update_servers(self,servers=None):
        servers = self.serversdata if servers is None else servers
        lst = []
        self.servers = servers
        for server in servers:
            serverContainer = Container()
            serverColumn = Column()
            serverName = Text(value=server.host)
            serverName.on_click = lambda e:print('clicked on that server...')
            serverButton = ElevatedButton(text='CONNECT',bgcolor=colors.ORANGE)
            serverColumn.controls = [serverName,serverButton]
            serverContainer.content = serverColumn
            lst.append(serverContainer)
        self.servers = lst
        return self.getservers()

    def update(self):
        self.servers_container.update()

    def append_to(self,target):
        self.container.width = target.width
        self.servers_container.width = target.width
        self.container.height = target.height
        self.servers_container.height = target.height
        target.controls.append(self.container)
        