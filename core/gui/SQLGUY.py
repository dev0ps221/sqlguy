from core.gui.Servers import ServersView
from core.gui.ServerActions import ServerActionsView
from flet import Page,Column,Container,Row,Text,ElevatedButton,colors
from mysql.connector.cursor_cext import CMySQLCursor as CMySQLCursor




class SQLGUY:


    connected_servers = []
    is_logged = None
    actual_server = None
    actual_view = 'login'
    topbarcontainer = Row()
    middlecontainer = Row()
    viewcontainer = Container(bgcolor=colors.BLUE_GREY_100,padding=20)
    view = Column(scroll='adaptive')
    serverscontainer = Container(bgcolor=colors.BLUE_GREY_200)
    serverscolumn = Column()
    container = Column()

    def list_databases(self):
        if self.actual_server:
            self.ServerActions.serveractions_container_label.value = self.actual_server
            self.view.controls = []
            for db in self.actual_server.getdatabases():
                dbrow = Row()
                dbname = Text(value=db.name)
                dabactions = Row()
                rename_database_button = ElevatedButton(text='rename database')
                drop_database_button = ElevatedButton(text='drop database')
                list_tables_button = ElevatedButton(text='list tables')
                dbrow.controls = [dbname]
                self.view.controls.append(dbrow)
            self.view.update()
            print('lets show the databases...')

    def create_database(self):
        if self.actual_server:
            self.ServerActions.serveractions_container_label.value = self.actual_server
            self.view.controls = []
            self.view.update()
            print('lets create a database...')

    def select_server(self,idx):
        self.actual_server = self.connected_servers[idx]
        self.ServerActions.update()
        self.refresh_view()

    def connect_server(self,event,serverinstance,serverscontainer,serverButton,selectButton):
        try:
            cursor = serverinstance.start()
        except Exception as e:
            cursor = None
        if type(cursor) is CMySQLCursor:
            self.connected_servers.append(serverinstance)
            serveridx = len(self.connected_servers) - 1 
            serverButton.bgcolor = colors.RED_200
            selectButton.disabled = False
            selectButton.on_click = lambda x:self.select_server(serveridx)
            serverButton.text = "DISCONNECT"
            serverscontainer.update()

    def refresh_view(self):
        self.topbarcontainer.update()
        self.serverscontainer.update()
        self.refresh()
        

    def build_components(self):
        self.ServerActions   =   ServerActionsView(self)
        self.Servers  =   ServersView(self)
        self.page.clean()
        self.viewcontainer.content = self.view
        self.container.width = self.wwidth()
        self.container.height = self.wheight()
        
        self.topbarcontainer.width = self.wwidth()
        self.topbarcontainer.height = int(self.wheight() *(15/100))
        self.middlecontainer.width = self.wwidth() 
        self.middlecontainer.height = int(self.wheight() *(85/100))
   
        self.viewcontainer.width = int(self.wwidth()*(70/100))
        self.serverscontainer.width = int(self.wwidth()*(30/100))
        self.view.width = int(self.wwidth()*(70/100))
        self.serverscolumn.width = int(self.wwidth()*(30/100))
   
        self.middlecontainer.controls = [self.viewcontainer,self.serverscontainer]
        self.container.controls = [self.topbarcontainer,self.middlecontainer]
        self.middlecontainer.padding = 0
        self.container.padding = 0
        self.serverscontainer.content = self.serverscolumn
        self.page.add(self.container)
        self.topbarcontainer.clean()
        self.serverscontainer.clean()
        self.ServerActions.append_to(self.topbarcontainer)        
        self.Servers.append_to(self.serverscolumn)

    def refresh(self):
        self.page.update()

    def wwidth(self):
        return int(self.page.window_width)

    def wheight(self):
        return int(self.page.window_height)

    def loop(self,page:Page):
        self.page = page
        self.page.bgcolor = colors.BLUE_GREY_100
        self.page.padding = 0
        self.build_components()
        self.refresh_view()