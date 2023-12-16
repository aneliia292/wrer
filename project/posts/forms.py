from django import forms

class AddPost(forms.Form):
    category = forms.CharField()
    title = forms.CharField()
    text = forms.CharField()
