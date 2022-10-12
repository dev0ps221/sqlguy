from core.gui.Servers import ServersView
from core.gui.ServerActions import ServerActionsView
from flet import Page,Column,Container,Row,Text,ElevatedButton,colors,alignment
from mysql.connector.cursor_cext import CMySQLCursor as CMySQLCursor





class SQLGUY:

    Servers = None
    ServerActions = None
    connected_servers = []
    is_logged = None
    actual_server = None
    actual_database = None
    actual_view = None
    topbarcontainer = Row()
    middlecontainer = Row()
    viewcontainer = Container(bgcolor=colors.BLUE_GREY_100,padding=5)
    viewcolumn = Column()
    viewlabel = Container(bgcolor=colors.WHITE)
    viewlabeltext = Text()
    view = Column(scroll='adaptive')
    serverscontainer = Container(bgcolor=colors.BLUE_GREY_200)
    serverscolumn = Column()
    container = Column()

    def list_database(self):
        if self.actual_server and self.actual_database:
            self.viewlabeltext.value = f"tables in {self.actual_server}{self.actual_database}"
            self.ServerActions.serveractions_container_label.value = f"{self.actual_server}{self.actual_database}"
            self.view.controls = self.actual_database.tablelistView(self)
            self.view.update()

    def create_database(self):
        if self.actual_server:
            self.viewlabeltext.value = f"create a new table in {self.actual_server}{self.actual_database}"
            self.ServerActions.serveractions_container_label.value = f"{self.actual_server}{self.actual_database}"
            self.ServerActions.serveractions_container_label.value = self.actual_server
            self.view.controls = self.actual_database.createtableView(self)
            self.view.update()
            

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
        if self.ServerActions is None and self.Servers is None:
            self.ServerActions   =   ServerActionsView(self)    
            self.Servers  =   ServersView(self)
        self.page.clean()
        self.viewcontainer.content = self.viewcolumn
        self.viewlabel.content = self.viewlabeltext
        self.viewcolumn.controls = [self.viewlabel,self.view]
        self.container.width = self.wwidth()
        self.container.height = self.wheight()
        
        self.topbarcontainer.width = self.wwidth()
        self.topbarcontainer.height = int(self.wheight() *(15/100))
        self.middlecontainer.width = self.wwidth() 
        self.middlecontainer.height = int(self.wheight() *(85/100))
   
        self.viewcontainer.width = int(self.wwidth()*(70/100))
        self.serverscontainer.width = int(self.wwidth()*(30/100))
        self.viewcontainer.height = self.middlecontainer.height
        self.view.width = int(self.wwidth()*(70/100))
        self.viewlabel.width = self.middlecontainer.width
        self.viewlabel.height = int(self.viewcontainer.height*5/100)
        self.viewlabeltext.width = self.middlecontainer.width
        self.viewlabeltext.height = int(self.viewcontainer.height*5/100)
        self.viewlabel.bgcolor = colors.WHITE
        self.view.height = int(self.viewcontainer.height*95/100)
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

    def on_resize(self,event):
        self.serverscolumn.clean()
        self.build_components()
        self.topbarcontainer.update()
        self.serverscontainer.update()
        self.refresh_view()

    def wwidth(self):
        return int(self.page.window_width)

    def wheight(self):
        return int(self.page.window_height)

    def loop(self,page:Page):
        self.page = page
        self.page.on_resize = self.on_resize
        self.page.bgcolor = colors.BLUE_GREY_100
        self.page.padding = 0
        self.build_components()
        self.refresh_view()