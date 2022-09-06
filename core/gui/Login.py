from flet import Text, TextField, ElevatedButton, Column, Row, Container, colors





class LoginView:


    def __init__(self,master):
        self.master = master

    def do_login(self,e):
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
        self.server_input = TextField(label='server')
        self.username_input = TextField(label='username')
        self.password_input = TextField(label='password')
        self.dologin_input = ElevatedButton(on_click=self.do_login,text='Se Connecter')
        self.form = Column()
        self.login_label_container.content = self.login_label
        self.server_container.content = self.server_input
        self.username_container.content = self.username_input
        self.password_container.content = self.password_input
        self.dologin_container.content = self.dologin_input
        self.form.controls = [self.login_label_container,self.server_container,self.username_container,self.password_container,self.dologin_container]
        self.container.content = self.form

    def update_form(self):
        self.form.update()

    def append_to(self,target):
        target.add(self.container)