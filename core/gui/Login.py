from flet import Text, TextEntry, ElevatedButton, Column, Row, Container, colors





class LoginView:


    def __init__(self,master):
        self.master = master

    def do_login(self):
        print(self.server_input.value)
        print(self.username_input.value)
        print(self.password_input.value)

    def build_components(self):
        self.container = Container()
        self.server_container = Container()
        self.login_label_container = Container()
        self.username_container = Container()
        self.password_container = Container()
        self.dologin_container = Container()
        self.login_label = Text(value='SE CONNECTER A UN SERVEUR DE BASE DE DONNÉES')
        self.server_input = TextEntry(label='server')
        self.username_input = TextEntry(label='username')
        self.password_input = TextEntry(label='password')
        self.dologin_input = ElevatedButton(on_click=self.do_login)
        self.form = Column()
        self.login_label_container.content = login_label
        self.server_container.content = server_input
        self.username_container.content = username_input
        self.password_container.content = password_input
        self.dologin_container.content = dologin_input
        self.form.controls = [self.login_label_container,self.server_container,self.username_container,self.password_container,self.dologin_container]
        self.container.content = self.form

    def update_form(self):
        self.form.update()

    def append_to(self,target):
        self.target.add(self.container)