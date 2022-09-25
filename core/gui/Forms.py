from core.classes.Form import FormView
class ServerForm:
    fields_template = [
        {
            'type':'text',
            'label':'host',
            'name':'host'
        },
        {
            'type':'text',
            'label':'username',
            'name':'username'
        },{
            'type':'text',
            'label':'password',
            'name':'password',
            'password':True,
            'can_reveal_password':True
        }
    ]
    
    def __init__(self,OnSubmit):
        self.formview = FormView(self.fields_template,OnSubmit=OnSubmit)
