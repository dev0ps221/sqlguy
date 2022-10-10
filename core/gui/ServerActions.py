from flet import Text, TextField, ElevatedButton, Column, Row, Container, colors,Dropdown,dropdown
from core.classes.ServerInstance import ServerInstance




class ServerActionsView:
    lasttarget = None
    server = None
    selected_database = None
    selected_view = None
    serveractions_container_label=Text(value='DATABASES')
    serveractions = Row(scroll='adaptive')
    serveractions_container = Column()
    container = Container(bgcolor=colors.BLUE_GREY_200,padding=5)
    databaselist = []
    databaseselect = Dropdown(label='SELECT DATABASE')
    listdatabasebutton = ElevatedButton(text='list')
    listdatabasebutton.bgcolor = colors.WHITE
    createdatabasebutton = ElevatedButton(text='create')
    createdatabasebutton.bgcolor = colors.WHITE

    def __init__(self,master,server=None):
        self.master = master
        self.server = server
        self.serveractions_container.controls = []
        self.listdatabasebutton.on_click=lambda x :self.on_select_view(x,x.control.text)
        self.createdatabasebutton.on_click=lambda x :self.on_select_view(x,x.control.text)
        
    def update(self):
        self.container.clean()
        self.container.clean()
        self.build_components()
        self.container.update()
        self.master.page.update()

    def select_database(self,name):
        for database in self.getdatabases():
            if database.name == name:
                self.master.actual_database = database
                self.selected_database = self.master.actual_database
        self.update()

    def select_view(self,view):
        self.selected_view = view
        self.update()
        self.serveractions.update()

    def getdatabases(self):
        return self.master.actual_server.getdatabases() if self.master.actual_server else []

    def on_select_view(self,event,view):
        self.select_view(view)
            
    def trigger_list_database(self):
        self.master.list_database()

    def trigger_create_database(self):
        self.master.create_database()
        
    def updatedatabaselist(self):
        self.databaselist = self.master.actual_server.getdatabases()

    def build_components(self):
        if self.master.actual_server:
            self.updatedatabaselist()
            self.databaseselect.options = []
            for database in self.databaselist:
                option = dropdown.Option(database) 
                if self.selected_database is not None:
                    self.databaseselect.value = database
                self.databaseselect.options.append(option)
            self.serveractions.controls = []
            self.serveractions.controls.append(self.databaseselect)
            self.serveractions.controls.append(self.listdatabasebutton)
            self.serveractions.controls.append(self.createdatabasebutton)
            self.serveractions_container.controls = [self.serveractions_container_label,self.serveractions]
            if self.selected_view:
                if self.selected_view == self.listdatabasebutton.text:
                    self.listdatabasebutton.bgcolor = colors.GREEN_100
                    if self.selected_database == None:
                        if len(self.databaselist):
                            self.select_database(self.databaselist[0].name)
                    else:
                        self.trigger_list_database()
                else:
                    self.listdatabasebutton.bgcolor = colors.WHITE

                if self.selected_view == self.createdatabasebutton.text:
                    self.createdatabasebutton.bgcolor = colors.GREEN_100
                    self.trigger_create_database()        
                else:
                    self.createdatabasebutton.bgcolor = colors.WHITE
        self.container.content = self.serveractions_container

        if self.master.actual_server:
            if self.selected_view is None :
                self.select_view('list')
        
        if self.lasttarget:
            self.append_to(self.lasttarget)
            self.lasttarget.update()
        

    def update_form(self):
        self.form.update()

    def append_to(self,target):
        self.lasttarget = target
        target.controls = []
        self.container.width = target.width
        self.serveractions_container.width = target.width
        self.container.height = target.height
        self.serveractions_container.height = target.height
        target.controls.append(self.container)