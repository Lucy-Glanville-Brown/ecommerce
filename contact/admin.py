from django.contrib import admin
from .forms import ContactForm
from .models import Contact


class ContactFormAdmin(admin.ModelAdmin):
    """ Admin for the contact form """

    list_display = (
        'name',
        'email',
        'subject',
        'message',
    )

    ordering = ('created_on',)


admin.site.register(Contact, ContactFormAdmin)
