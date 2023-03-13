from django.contrib import admin

# Register your models here.


from .models import PersonName

admin.site.register(PersonName)