from django.contrib import admin

# Register your models here.

from .models import Menu ,Order
# import the Menu and Order from the models.py file 

admin.site.register(Menu)
#register the Menu in admin panel
admin.site.register(Order)
# register the Order in admin panel
