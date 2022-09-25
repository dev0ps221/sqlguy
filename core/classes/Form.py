from flet import TextField,ElevatedButton,Column
class FieldElem:
    elem = None
    def __init__(self,data):
        self.data = data
        self.build_elem()

    def build_elem(self):
        if 'type' in self.data:
            if self.data['type'] == 'text':
                self.elem = TextFieldElem(self.data)

class TextFieldElem:
    data = {}
    elem = TextField() 

    def set_data(self,data):
        self.rawdata = data
        for key in data.keys():
            self.data[key] = data[key]

    def build_elem(self):
        if 'password' in self.data:
            self.elem.password = self.data['password']
            if 'can_reveal_password' in self.data:
                self.elem.can_reveal_password =  self.data['can_reveal_password']
        if 'label' in self.data:
            self.elem.label = self.data['label']

    def __init__(self,data):
        self.set_data(data)
        self.build_elem()

class FormView:
    field_elems = []
    submitButton = ElevatedButton(text='ok')
    container = Column()
    

    def append_to(self,target):
        self.container.width = target.width
        target.controls.append(self.container)

    def setOnSubmit(self,action,text=None):
        if text is not None:
            self.submitButton.text = text
            self.submitButton.on_click = action

    def build_field_elem(self,field):
        return FieldElem(field)

    def assign_fields(self):
        for field in self.fields: 
            field_elem = self.build_field_elem(field)
            self.field_elems.append(field_elem)

    def mount_fields(self):
        controls = []
        for elem in self.field_elems:
            field_elem = elem.elem.elem
            controls.append(field_elem)
        controls.append(self.submitButton)
        self.container.controls = controls

    def refresh(self):
        self.container.update() 

    def __init__(self,fields):
        print(fields)
        self.fields = fields
        print(self.field_elems)
        self.assign_fields()
        self.mount_fields()
