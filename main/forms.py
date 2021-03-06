from .models import Comment
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'website', 'body')

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control comment-form-name-input',
                'placeholder': 'Name*',
            }),
            "email": EmailInput(attrs={
                'class': 'form-control comment-form-email-input',
                'placeholder': 'Email*',
            }),
            "website": TextInput(attrs={
                'class': 'form-control comment-form-website-input',
                'placeholder': 'Website',
            }),
            "body": Textarea(attrs={
                'class': 'form-control comment-form-body-input',
                'placeholder': 'Comment*',
            }),
        }

