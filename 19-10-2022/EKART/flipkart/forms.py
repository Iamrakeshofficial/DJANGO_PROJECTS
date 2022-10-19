from django import forms

from .models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

        labels = {'name': 'Enter Name', 'phone': 'Enter Phone No', 'email': 'Enter EMail Id','message':'Enter message','address':'Enter Address'}
        error_messages = {
            'name': {'required': 'Give your name'}}

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }