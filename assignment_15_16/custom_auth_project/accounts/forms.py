from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'auth-input'
            }),
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Full Name',
                'class': 'auth-input'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ვშლი label-ებს და ვამატებ class-ებს და placeholder-ებს
        self.fields['email'].label = ""
        self.fields['full_name'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""

        self.fields['password1'].widget.attrs.update({
            'class': 'auth-input',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'auth-input',
            'placeholder': 'Confirm Password'
        })


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ვშლი label-ებს და ვამატებ class-ებს და placeholder-ებს჻
        self.fields['username'].label = ""
        self.fields['password'].label = ""

        self.fields['username'].widget.attrs.update({
            'class': 'auth-input',
            'placeholder': 'Email'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'auth-input',
            'placeholder': 'Password'
        })