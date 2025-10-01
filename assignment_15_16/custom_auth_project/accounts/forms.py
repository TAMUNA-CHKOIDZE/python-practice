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


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("No user with this email.")
        return email


class SetNewPasswordForm(forms.Form):
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("new_password1")
        p2 = cleaned_data.get("new_password2")

        if p1 != p2:
            raise forms.ValidationError("Passwords do not match.")
        if p1 and len(p1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters.")
        return cleaned_data
