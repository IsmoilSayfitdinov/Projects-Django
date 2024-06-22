from django import forms
from .models import ContactsGetdataModel


class ContactsForm(forms.ModelForm):
    class Meta:
        model = ContactsGetdataModel
        fields = "__all__"