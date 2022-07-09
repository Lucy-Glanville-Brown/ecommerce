from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


# Credit - https://docs.djangoproject.com/en/4.0/topics/forms/
def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # ...
            send_mail(
                f'Message from {name}, {email} about {subject}',
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER]
            )
            messages.success(
                request, 'Your message has been sent!')
            # redirect to contact page
            return redirect(reverse('contact'))
        else:
            messages.error(
                request, 'There was a problem sending your message. \
                    Please try again.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
