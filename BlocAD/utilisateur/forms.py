from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
  username= forms.CharField(label="Nom d'utilisateur", 
                            widget=forms.TextInput(
                               attrs={
                                 "class": "Form-control"
                                 }
                                 ))
  password= forms.CharField(label="Mot de passe", 
                            widget=forms.PasswordInput(
                               attrs={
                                 "class": "Form-control"
                                 }
                                 ))

  
class SignUpForm(UserCreationForm):
  username= forms.CharField(label="Nom d'utilisateur", 
                            widget=forms.TextInput(
                               attrs={
                                 "class": "Form-control"
                                 }
                                 ))
  email= forms.EmailField(label="Email", 
                            widget=forms.EmailInput(
                               attrs={
                                 "class": "Form-control"
                                 }
                                 ))
  password1= forms.CharField(label="Mot de passe", 
                            widget=forms.PasswordInput(
                               attrs={
                                 "class": "Form-control"
                                 }
                                 ))
  password2= forms.CharField(label="Confirmer votre de passe", 
                            widget=forms.PasswordInput(
                               attrs={
                                 "class": "Form-control"
                                 }
                                 ))