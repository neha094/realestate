from django.contrib import admin
from .models import Calc

class CalcAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'calc_date')
    list_display_links = ('id', 'name')
    search_fields = ( 'name', 'required', 'listing')
    list_per_page = 25

admin.site.register(Calc, CalcAdmin)