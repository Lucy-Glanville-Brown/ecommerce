from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """ Admin setting to display a list of reviews """

    model = Review
    list_display = (
        'product',
        'created_on',
        'stars',
        'user',
        'comment',
    )

    ordering = ('created_on',)


admin.site.register(Review, ReviewAdmin)
