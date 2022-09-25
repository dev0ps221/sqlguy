
class FieldElem:
    elem = None
    def __init__(self,data):
        self.data = data

    def build_elem(self):
        if 'type' in self.data:
            if self.data['type'] == 'text':
                self.elem = TextFieldElem(self.data)

class TextFieldElem:
    data = {}
    elem = Text() 

    def set_data(self,data):
        self.rawdata = data
        for key in data.keys():
            self.data[key] = key

    def build_elem(self):
        for key in self.data:
            elem[:key] = self.data[:key]

    def __init__(self,data):
        self.set_data(data)
        self.build_elem()

class FormView:
    field_elems = {}

    def build_field_elem(self,field):


    def __init__(self,fields):
        self.fields = fields