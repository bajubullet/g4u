from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class SignupForm(forms.Form):
    '''
    Signup form for user.
    '''
    first_name = forms.CharField(label=_('first name'))
    last_name = forms.CharField(label=_('last name'))
    username = forms.CharField(label=_('username'))
    password1 = forms.CharField(label=_('password'), widget=forms.widgets.PasswordInput())
    password2 = forms.CharField(label=_('confirm password'), widget=forms.widgets.PasswordInput())
    email = forms.EmailField(label=_('e-mail'))
    location = forms.CharField(label=_('location'),
        help_text=_('You location helps us suggest gamers and events near you.'))
    phone_number = forms.CharField(label=_('phone number'))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            return forms.ValidationError(_('The two passwords do not match.'))

    def clean_email(self):
        if User.objects.filter(email__exact=self.cleaned_data['email']).exists():
            return forms.ValidationError(_('A user with that email already exists.'))

    def save(self):
        '''
        Creates new user.
        '''
        if self.is_valid():
            data = self.cleaned_data
            user = User.objects.create_user(
                data['username'],
                password = data['password1'],
                email= data['email'],
                first_name = data['first_name'],
                last_name = data['last_name'],
            )
            return user
