from flet import Text, TextEntry, ElevatedButton, Column, Row, Container, colors





class ServerView:

    def __init__(self,master):
        self.master = master

    def do_logout(self):
        pass

    def build_components(self):
        self.container = Container()
        self.server_container = Container()
        self.server_view = Row()
        self.server_container.controls = [self.server]
        self.container.content = self.server_container

    def update_server(self):
        self.server_view.update()

    def append_to(self,target):
        self.target.add(self.container)