from django.contrib import admin

# Register your models here.
from .models import Menu, Ingredients, Purchased

admin.site.register(Menu)
admin.site.register(Ingredients)
admin.site.register(Purchased)

