from django.contrib.auth import authenticate, login, logout
from django import forms
from .mail_sender import Mail_sender
from .models import *
import random

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['email', 'firstname', 'lastname', 'address', 'post_nr', 'post_place']
        widgets = {
            'email':forms.TextInput(attrs={'placeholder':'Epost'}),
            'firstname':forms.TextInput(attrs={'placeholder':'Fornavn'}),
            'lastname':forms.TextInput(attrs={'placeholder':'Etternavn'}),
            'address':forms.TextInput(attrs={'placeholder':'Leveringsadresse'}),
            'post_nr':forms.TextInput(attrs={'placeholder':'Postnr.', 'class':'short'}),
            'post_place':forms.TextInput(attrs={'placeholder':'Poststed', 'class':'short'}),
        }

    # Sets all the fields to required. Without using the html5 attribute wich does not work on iphones
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True

    def clean(self):
        cleaned_data = super(UserProfileForm, self).clean()
        if not cleaned_data.get("email"):
            raise forms.ValidationError("Vennligst skriv epostaddressen på nytt")
        email = cleaned_data.get("email").lower()
        if UserProfile.objects.filter(email=email).exists():
            raise forms.ValidationError('Emailen "%s" er allerede i bruk.' % email)
        return cleaned_data

    def save(self, company, commit=True):
        # Save the provided password in hashed format
        user = super(UserProfileForm, self).save(commit=False)
        password = generate_random()

        user.set_password(password)
        user.company = company
        user.email = user.email.lower()

        if commit:
            user.save()
            Mail_sender.send_welcome_mail(user, password)

            user = authenticate(username=user.email.lower(), password=password)

        return user


class LoginForm(forms.Form):
    username = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Epost'}),max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Passord'}), required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Ugyldig brukernavn eller passord")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


def generate_random():
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&?+'

    code = ''

    for i in range(0,10):
        rand = random.randint(0, 68)

        code += a[rand]

    return code