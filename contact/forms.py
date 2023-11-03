from django import forms
from .models import Contact
#Write Code here
class ContacForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"