def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
        field.widget.attrs['class'] = 'form-control'
    self.fields['turma'].required = False
    self.fields['papel'].choices = [
        (k, v) for k, v in self.fields['papel'].choices
        if k != 'admin'
    ]
