from django import forms
from django.core.exceptions import ValidationError
from pomagam_app.models import Donation


def password_validation(value):
    if len(value) < 2:
        raise ValidationError("za krótkie hasło co najmniej 6 znaków")


class RegisterForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, validators=[password_validation])
    re_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['re_password']:
                raise ValidationError("Hasła nie są identyczne")
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class AddDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ['user']
