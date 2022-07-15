from django import forms
from . models import Review


class ReviewForm(forms.ModelForm):
    """ Credit Bunny The Compiler """
    class Meta:
        model = Review
        fields = ["stars", "comment"]
