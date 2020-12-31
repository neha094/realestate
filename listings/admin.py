from django.contrib import admin
from .models import listing

# Register your models here.
class listingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
admin.site.register(listing, listingAdmin)
