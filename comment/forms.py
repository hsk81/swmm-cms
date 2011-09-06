from django import forms

class CommentForm (forms.Form):

    sender = forms.CharField (max_length=32)
    email = forms.EmailField ()
    message = forms.CharField (max_length=4096, widget=forms.Textarea)
