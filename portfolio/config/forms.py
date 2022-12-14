
from django import forms



class FormUser(forms.Form):
    nom = forms.CharField (max_length=30)
    prenom = forms.CharField (max_length=30)
    login = forms.CharField (max_length=10)
    mot2pass = forms.CharField (widget=forms.PasswordInput)
    confirm = forms.CharField (widget=forms.PasswordInput)
    email = forms.EmailField (max_length=200)
class FormConnexion(forms.Form):
    login = forms.CharField (max_length=10)
    mot2pass = forms.CharField (widget=forms.PasswordInput)
