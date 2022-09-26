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
        addserverlabelcontainer = Container(bgcolor=colors.WHITE)
        addserverlabeltext = Text(value='ADD A SERVER')
        addserverlabelcontainer.width = self.master.serverscolumn.width
        addserverlabelcontainer.alignment=alignment.center
        addserverlabelcontainer.content = addserverlabeltext
        self.servers_container.controls.append(addserverlabelcontainer)
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
            serverContainer = Container(bgcolor=colors.BLUE_500)
            serverColumn = Column()
            serverName = Text(value=server.__repr__())
            serverButton = ElevatedButton(text='CONNECT',bgcolor=colors.ORANGE)
            serverButton.on_click=lambda x: self.master.connect_server(server,self.servers_container,serverButton)
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
        