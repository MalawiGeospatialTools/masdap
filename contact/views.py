from django.http import HttpResponse
from contact.forms import ContactForm
from django.shortcuts import render, redirect

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib import messages

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission on MASDAP",
                content,
                'masdap.mw@gmail.com',
                ['masdap.mw@gmail.com'],
                cc=(contact_email,),
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.success(request, 'Contact email sent')
            return redirect('contact')
        else:
            messages.error(request, 'The form is not valid. Please fill it in correctly and send it again.')
    return render(request, 'contact.html', {
        'form': form_class,
    })
