from django.db import models

class Contact(models.Model):
    """ Model to record the contact form """

    class Meta:
        """ Set verbose name """
        verbose_name = 'Contact Form'
        verbose_name_plural = 'Contact Forms'

    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.CharField(max_length=300, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "-" + self.subject