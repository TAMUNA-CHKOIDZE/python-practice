import re

from django import forms

from userform.models import UserSubmission


class UserSubmissionForm(forms.ModelForm):
    class Meta:
        model = UserSubmission
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter your name',
                'class': 'form-control',  #კლასი
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control', #კლასი
            }),
        }

    # დამატებითი ვალიდაცია არ არის დავალების მოთხოვნაში, მაგრამ ვაკეთებ მინიმალური სიგრძის შემოწმებას. ასევე regex უშვებს ქართულ და ინგლისურ ასოებს, სივრცეს და დეფისს (მაგ: გიორგი-ნიკა)
    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()

        if len(username) < 2:
            raise forms.ValidationError("Please enter a valid name.")

        if not re.match(r'^[ა-ჰa-zA-Z\s\-]+$', username):
            raise forms.ValidationError("Name can only contain Georgian or English letters, spaces, or hyphens.")

        return username
