from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.core import validators
from django import forms
from django.db import transaction
from .models import *

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    verify_password = forms.CharField(widget=forms.PasswordInput())
    verify_password = forms.CharField(widget=forms.PasswordInput())
    doctor_id = forms.CharField()
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password','verify_password','city','state','address','phone_number','is_patient','is_doctor')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.set_password(user.password)
        user.save()
        user.Age =self.cleaned_data.get('Age')
        user.city=self.cleaned_data.get('city')
        user.state=self.cleaned_data.get('state')
        user.address=self.cleaned_data.get('address')
        user.phone_number=self.cleaned_data.get('phone_number')
        user.is_patient=self.cleaned_data.get('is_patient')
        user.is_doctor=self.cleaned_data.get('is_doctor')

        user.save()
        return user