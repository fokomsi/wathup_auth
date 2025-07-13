from allauth.account.forms import LoginForm, SignupForm
from django import forms

class BootstrapLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ajouter les classes Bootstrap
        self.fields['login'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Email ou nom d\'utilisateur'
        })
        
        self.fields['password'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Mot de passe'
        })
        
        self.fields['remember'].widget.attrs.update({
            'class': 'form-check-input'
        })


class BootstrapSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30, 
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Prénom'
        })
    )
    
    last_name = forms.CharField(
        max_length=30, 
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nom'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Ajouter les classes Bootstrap aux champs existants
        field_classes = {
            'email': 'form-control form-control-lg',
            'username': 'form-control form-control-lg',
            'password1': 'form-control form-control-lg',
            'password2': 'form-control form-control-lg'
        }
        
        placeholders = {
            'email': 'Votre adresse email',
            'username': 'Nom d\'utilisateur',
            'password1': 'Mot de passe',
            'password2': 'Confirmer le mot de passe'
        }
        
        for field_name, field in self.fields.items():
            if field_name in field_classes:
                field.widget.attrs.update({
                    'class': field_classes[field_name],
                    'placeholder': placeholders.get(field_name, '')
                })
            elif field_name not in ['first_name', 'last_name']:
                field.widget.attrs.update({
                    'class': 'form-control'
                })

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        return user


# Formulaire de réinitialisation de mot de passe
class BootstrapResetPasswordForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Votre adresse email'
        })
    )


# Formulaire de changement de mot de passe
class BootstrapChangePasswordForm(forms.Form):
    oldpassword = forms.CharField(
        label="Ancien mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Ancien mot de passe'
        })
    )
    
    password1 = forms.CharField(
        label="Nouveau mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Nouveau mot de passe'
        })
    )
    
    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Confirmer le nouveau mot de passe'
        })
    )


# Formulaire de profil utilisateur
class UserProfileForm(forms.ModelForm):
    class Meta:
        from django.contrib.auth.models import User
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prénom'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})