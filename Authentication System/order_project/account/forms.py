from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account
from order.models import Floor
from django import forms


class RegistrationForm(UserCreationForm):
    email       = forms.EmailField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
            'type': 'email',
            'autofocus': '',
        })
    )
    username    = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'type': 'username',
        })
    )
    password1    = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'type': 'password',
        })
    )
    password2    = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repeat Password',
            'type': 'password',
        })
    )

    floors      = forms.ModelChoiceField(
        queryset=Floor.objects.all(),
        empty_label="Select Your Floor",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    class Meta:
        model = Account
        fields = ['email', 'username', 'password1', 'password2']


class AccountAuthenticationForm(forms.ModelForm):
    email = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
            'type': 'email',
            'autofocus': '',
        })
    )
    password = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'type': 'password',
        })
    )


    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid email or password')
