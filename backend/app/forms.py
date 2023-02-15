from django import forms


class JsonImportForm(forms.Form):
    json_upload = forms.FileField()