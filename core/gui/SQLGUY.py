from core.gui.Servers import ServersView
from core.gui.Databases import DatabasesView
from flet import Page,Column,Container,Row,Text,ElevatedButton






class SQLGUY:

    connected_servers = []
    is_logged = None
    actual_server = None
    actual_view = 'login'
    topbarcontainer = Row()
    middlecontainer = Row()
    viewcontainer = Column()
    serverscontainer = Column()
    container = Column()
     
    def refresh_view(self):
        

    def __init__(self):
        self.Databases   =   DatabasesView(self)
        self.Servers  =   ServersView(self)
        self.build_components()
    def build_components(self):


    def loop(self,page:Page):
        self.page = page
        self.refresh_view()