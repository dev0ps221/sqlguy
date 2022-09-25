from core.classes.Form import FormView
class ServerForm:
    fields_template = [
        {
            'type':'text',
            'label':'host'
        },
        {
            'type':'text',
            'label':'username'
        },{
            'type':'text',
            'label':'password',
            'password':True,
            'can_reveal_password':True
        }
    ]
    
    def __init__(self,OnSubmit):
        self.formview = FormView(self.fields_template,OnSubmit=OnSubmit)
