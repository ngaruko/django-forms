from django.contrib import admin

from .models import Customer, Size, Flavour, Coffee

admin.site.register(Customer)
admin.site.register(Size)
admin.site.register(Flavour)
admin.site.register(Coffee)