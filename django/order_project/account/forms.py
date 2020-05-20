from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import authenticate

from account.models import Account
from order.models import Floor


class RegistrationForm(auth_forms.UserCreationForm):
    email           = forms.EmailField(
                        max_length=60,
                        widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Email Address',
                            'type': 'email',
                            'autofocus': True,
                        })
                    )
    username        = forms.CharField(
                        max_length=30,
                        widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Username',
                            'type': 'username',
                        })
                    )
    password1       = forms.CharField(
                        max_length=30,
                        widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Password',
                            'type': 'password',
                        })
                    )
    password2       = forms.CharField(
                        max_length=30,
                        widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Repeat Password',
                            'type': 'password',
                        })
                    )

    class Meta:
        model   = Account
        fields  = ['email', 'username', 'password1', 'password2']


class SignInForm(forms.Form):
    email           = forms.CharField(
                        max_length=60,
                        widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Email Address',
                            'type': 'email',
                            'autofocus': True,
                        })
                    )
    password        = forms.CharField(
                        widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Password',
                            'type': 'password',
                        })
                    )


    class Meta:
        model   = Account
        fields  = ('email', 'password')

    def clean(self):
        email    = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid email or password')


class PasswdChangeForm(auth_forms.PasswordChangeForm):
    old_password    = forms.CharField(
                        widget=forms.PasswordInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Old Password',
                            'autocomplete': 'current-password',
                            'autofocus': True,
                            }),
                    )
    new_password1   = forms.CharField(
                        widget=forms.PasswordInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'New Password',
                            }),
                    )
    new_password2   = forms.CharField(
                        widget=forms.PasswordInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Confirm Password',
                            }),
                    )


class PasswdResetForm(auth_forms.PasswordResetForm):
    email           = forms.EmailField(
                        widget=forms.EmailInput(attrs={
                            'autocomplete': 'email',
                            'class': 'form-control',
                            'placeholder': 'Email address',
                            'autofocus': True,
                            })
                    )


class PasswdResetConfirmForm(auth_forms.SetPasswordForm):
    new_password1   = forms.CharField(
                        widget=forms.PasswordInput(attrs={
                            'autocomplete': 'new-password',
                            'class': 'form-control',
                            'placeholder': 'New Password',
                            'autofocus': True
                            }),
                    )
    new_password2   = forms.CharField(
                        widget=forms.PasswordInput(attrs={
                            'autocomplete': 'new-password',
                            'class': 'form-control',
                            'placeholder': 'Repeat Password',
                            }),
                    )
