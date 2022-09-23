from core.gui.Servers import ServersView
from core.gui.Databases import DatabasesView
from flet import Page,Column,Container,Row,Text,ElevatedButton,colors






class SQLGUY:

    connected_servers = []
    is_logged = None
    actual_server = None
    actual_view = 'login'
    topbarcontainer = Row()
    middlecontainer = Row()
    viewcontainer = Container(expand=True,bgcolor=colors.BLUE_200)
    view = Column()
    serverscontainer = Column()
    container = Column()
     
    def refresh_view(self):
        self.topbarcontainer.clean()
        self.serverscontainer.clean()
        self.Databases.append_to(self.topbarcontainer)        
        self.Servers.append_to(self.serverscontainer)        
        self.topbarcontainer.update()
        self.serverscontainer.update()
    def __init__(self):
        self.Databases   =   DatabasesView(self)
        self.Servers  =   ServersView(self)

    def build_components(self):
        self.page.clean()
        self.viewcontainer.content = self.view
        self.middlecontainer.controls = [self.viewcontainer,self.serverscontainer]
        self.container.controls = [self.topbarcontainer,self.middlecontainer]
        self.page.add(self.container)
        self.refresh()

    def refresh(self):
        self.page.update()
    
    def loop(self,page:Page):
        self.page = page
        self.build_components()
        self.refresh_view()