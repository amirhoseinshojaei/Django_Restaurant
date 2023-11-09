from django import forms
from .models import Comment
########
class CommentForm(forms.ModelForm):
    class Meat:
        model = Comment
        fields = [
            'name',
            'email',
            'message',
            'blog'
        ]
        widgets = {
            'blog': forms.HiddenInput()
        }