from core.gui.Login  import   LoginView
from core.gui.Server import ServerView
from flet import Page






class SQLGUY:

    connected_servers = []
    is_logged = None
    actual_server = None
    actual_view = 'login'
    def set_actual_server(self,idx):
        if idx >= 0 and idx < len(self.connected_servers):
            self.actual_server = self.connected_servers[idx]

    def just_logged(self,server):
        if server:
            self.connected_servers.append(server)
            self.set_actual_server(len(self.connected_servers)-1)
            self.set_view('server')
        self.refresh_view()

    def set_view(self,view):
        self.actual_server = view

    def login_view(self):
        self.Login.build_components()
        self.Login.append_to(self.page)

    def server_view(self):
        self.Server.build_components()
        self.Server.append_to(self.page)

    def refresh_view(self):
        if self.actual_view == 'login':
            self.login_view()

        if self.actual_view == 'server':
            self.server_view()

    def __init__(self):
        self.Login   =   LoginView(self)
        self.Server  =   ServerView(self)
        self.set_view('login')

    def loop(self,page:Page):
        self.page = page
        self.refresh_view()