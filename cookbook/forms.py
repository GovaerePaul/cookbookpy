from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from cookbook.models import Recette, Note


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class RecetteForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Recette
        fields = ['titre', 'type', 'difficulte', 'cout', 'temps_prepa', 'temps_cuisson', 'temps_repos','ingredients','etape']


class InscriptionForm(UserCreationForm):
    required_css_class = 'required'
    last_name = forms.CharField(required=True, label="Nom")
    first_name = forms.CharField(required=True, label="Prenom")
    email = forms.EmailField(required= True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def save(self, commit=True):
            user = super(InscriptionForm, self).save(commit=False)
            user.nom = self.cleaned_data['last_name']
            user.prenom = self.cleaned_data['first_name']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()
            return user

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'