from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            sender_message = form.cleaned_data['message']
            email = EmailMessage(
                "New contact form submission on MASDAP",
                sender_message,
                'masdap.mw@gmail.com',
                ['masdap.mw@gmail.com'],
                cc=(sender_email,),
                headers = {'Reply-To': sender_email}
            )
            email.send()

            messages.success(request, 'Thanks for reaching out! Your message has been sent.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form
    })
