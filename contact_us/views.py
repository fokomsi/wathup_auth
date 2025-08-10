from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Sauvegarder le message
            contact = form.save()
            
            # Envoyer un email (optionnel)
            try:
                send_mail(
                    subject=f"Nouveau message de contact: {contact.sujet}",
                    message=f"""
                    Nom: {contact.nom}
                    Email: {contact.email}
                    Sujet: {contact.sujet}
                    
                    Message:
                    {contact.message}
                    """,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Erreur envoi email: {e}")
            
            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('home')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})




