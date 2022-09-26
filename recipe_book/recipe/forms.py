from django import forms
from .models import Menu, Ingredients, Purchased

class IngredientsCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields =('ingredients', 'price', 'amount', )

class IngredientsUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ('ingredients', 'price', 'amount', )


class MenuCreateForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('menu_item','price','amount', 'strength', 'ingred')

class MenuUpdateForm(forms.ModelForm):
    #form for updating owners
    class Meta:
        model = Menu
        fields = ('menu_item', 'price', 'amount', 'strength', 'ingred')

class PurchasedCreateForm(forms.ModelForm):
    class Meta:
        model = Purchased
        fields = ('order', 'price', 'amount')

class PurchasedUpdateForm(forms.ModelForm):
    #form for updating owners
    class Meta:
        model = Purchased
        fields = ('order', 'price', 'amount')

