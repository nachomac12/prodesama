from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Bet

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']  #cleaned_data me asegura que no se escriba sql por ejemplo
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class BetForm(forms.ModelForm):
    team1_score = forms.IntegerField(min_value=0, max_value=15)
    team2_score = forms.IntegerField(min_value=0, max_value=15)
    
    class Meta:
        model = Bet
        fields = ('team1_score', 'team2_score', 'match',)