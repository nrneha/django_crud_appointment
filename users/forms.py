from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from. models import *


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField()
    gender = forms.CharField()
    mobile_no = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username','email', 'age','gender','mobile_no','password1', 'password2']


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()  # Save User model first
            UserProfile.objects.create(
                user=user,
                age=self.cleaned_data['age'],
                gender=self.cleaned_data['gender'],
                mobile_no=self.cleaned_data['mobile_no']
            )
        return user