
from django.db import models
from django.contrib.auth.models import User

class Ingredients(models.Model):
    ingredients = models.CharField(max_length=20)
    price = models.IntegerField()
    amount = models.IntegerField()

    def get_absolute_url(self):
        return "/ingredients/list/"
    
    def __str__(self):
        return self.ingredients

class Menu(models.Model):
    menu_item = models.CharField(max_length=20)
    price = models.IntegerField(default=20)
    amount = models.IntegerField(default=20)
    strength = models.CharField(max_length=20, default='-')
    ingred = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return "/menu/list/"

    def __str__(self):
        return self.menu_item
    

class Purchased(models.Model):
    order = models.ForeignKey(Menu, on_delete=models.CASCADE)
    price = models.IntegerField(default=20)
    amount = models.IntegerField(default=20)

    def get_absolute_url(self):
        return "/purchased/list/"

   
    

    



