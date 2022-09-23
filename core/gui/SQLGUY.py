from core.gui.Servers import ServersView
from core.gui.Databases import DatabasesView
from flet import Page






class SQLGUY:

    connected_servers = []
    is_logged = None
    actual_server = None
    actual_view = 'login'
    
    def __init__(self):
        self.Databases   =   DatabasesView(self)
        self.Servers  =   ServersView(self)
        self.set_view('login')

    def loop(self,page:Page):
        self.page = page
        self.refresh_view()