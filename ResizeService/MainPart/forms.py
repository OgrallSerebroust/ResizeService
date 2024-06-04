from django import forms

class InsertImagesForm(forms.Form):
    urls = forms.CharField(initial="https://", label="Вставьте ссылки", widget=forms.Textarea)
    is_choose_resolution = forms.BooleanField(label="Выбрать размер", required=False)
    height = forms.IntegerField(label="Высота", min_value=1)
    weight = forms.IntegerField(label="Ширина", min_value=1)

    def __init__(self, *args, **kwargs) -> None:
        super(InsertImagesForm, self).__init__(*args, **kwargs)
        self.fields["urls"].widget.attrs.update({
            "style": "min-height: 200px;",
            "type": "email",
            "class": "form-control",
            "id": "floatingInput",
            "placeholder": ""
        })
        self.fields["height"].widget.attrs.update({
            "class": "form-control",
            "id": "floatingPassword",
            "placeholder": "Password",
            "value": "1200"
        })
        self.fields["weight"].widget.attrs.update({
            "class": "form-control",
            "id": "floatingPassword",
            "placeholder": "Password",
            "value": "1200"
        })
