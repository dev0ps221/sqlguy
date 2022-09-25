
class TextFieldElem:
    data = {}
    elem = None
    def build_elem(self):
        if 'type' in self.data:
        

    def set_data(self,data):
        self.rawdata = data
        for key in data.keys():
            self.data[key] = key

    def __init__(self,data):
        self.set_data(data)
    

class FormView:
    field_elems = {}

    def build_field_elem(self,field):


    def __init__(self,fields):
        self.fields = fields