
# Vues correspondantes (views.py)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .forms import BootstrapLoginForm, BootstrapSignupForm, UserProfileForm, BootstrapChangePasswordForm

def home(request):
    return render(request, 'user_page/home.html')

@login_required
def dashboard(request):
    return render(request, 'user_page/dashboard.html')

@login_required 
def profile(request):
    return render(request, 'user_page/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil mis à jour avec succès!')
            return redirect('votre_app:profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'edit_profile.html', {'form': form})

# Vues personnalisées (optionnel - si vous voulez surcharger les vues allauth)
def custom_login(request):
    if request.method == 'POST':
        form = BootstrapLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('votre_app:dashboard')
    else:
        form = BootstrapLoginForm()
    
    return render(request, 'account/login.html', {'form': form})

def custom_signup(request):
    if request.method == 'POST':
        form = BootstrapSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            messages.success(request, 'Compte créé avec succès!')
            return redirect('account_login')
    else:
        form = BootstrapSignupForm()
    
    return render(request, 'account/signup.html', {'form': form})

@login_required
def custom_password_change(request):
    if request.method == 'POST':
        form = BootstrapChangePasswordForm(request.POST)
        if form.is_valid():
            # Logique de changement de mot de passe
            messages.success(request, 'Mot de passe modifié avec succès!')
            return redirect('votre_app:profile')
    else:
        form = BootstrapChangePasswordForm()
    
    return render(request, 'account/password_change.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')