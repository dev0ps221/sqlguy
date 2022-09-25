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
    viewcontainer = Container(bgcolor=colors.GREEN_200)
    view = Column()
    serverscontainer = Container(bgcolor=colors.ORANGE_200)
    serverscolumn = Column()
    container = Column()
     
    def refresh_view(self):
        self.topbarcontainer.clean()
        self.serverscontainer.clean()
        self.Databases.append_to(self.topbarcontainer)        
        self.Servers.append_to(self.serverscolumn)        
        self.topbarcontainer.update()
        self.serverscontainer.update()
        self.page.update()
        
    def __init__(self):
        self.Databases   =   DatabasesView(self)
        self.Servers  =   ServersView(self)

    def build_components(self):
        self.page.clean()
        self.viewcontainer.content = self.view
        self.container.width = self.wwidth()
        self.container.height = self.wheight()
        
        self.topbarcontainer.width = self.wwidth()
        self.topbarcontainer.height = int(self.wheight() *(10/100))
        self.middlecontainer.width = self.wwidth() 
        self.middlecontainer.height = int(self.wheight() *(90/100))
   
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
        self.refresh()

    def refresh(self):
        self.page.update()
    
    def wwidth(self):
        return int(self.page.window_width)

    def wheight(self):
        return int(self.page.window_height)

    def loop(self,page:Page):
        self.page = page
        self.page.padding = 0
        self.build_components()
        self.refresh_view()