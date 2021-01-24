from django.contrib import admin

# Register your models here.
from .models import Workshop, Order

admin.site.register(Workshop)
admin.site.register(Order)
