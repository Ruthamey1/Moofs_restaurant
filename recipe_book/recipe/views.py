from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Ingredients, Menu, Purchased
from .forms import IngredientsCreateForm, IngredientsUpdateForm, MenuCreateForm, MenuUpdateForm, PurchasedCreateForm, PurchasedUpdateForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

def logout_view(request):
  logout(request)
  return redirect("home")

@login_required
def home(request):
   context = {"name": request.user, "purchased": Purchased}
   return render(request, "recipe/home.html", context)

class IngredientsList(LoginRequiredMixin, ListView):
   model = Ingredients

# Add your class below:
class IngredientsCreate(LoginRequiredMixin, CreateView):
  model = Ingredients
  template_name = "recipe/ingredients_create_form.html"
  form_class = IngredientsCreateForm

class IngredientsUpdate(LoginRequiredMixin, UpdateView):
   model = Ingredients
   template_name = "recipe/ingredients_update_form.html"
   form_class = IngredientsUpdateForm

class IngredientsDelete(LoginRequiredMixin, DeleteView):
    model = Ingredients
    template_name = "recipe/ingredients_delete_form.html"
    success_url = "/ingredients/list"

class MenuList(LoginRequiredMixin, ListView):
   model = Menu

# Add your class below:
class MenuCreate(LoginRequiredMixin, CreateView):
  model = Menu
  template_name = "recipe/menu_create_form.html"
  form_class = MenuCreateForm

class MenuUpdate(LoginRequiredMixin, UpdateView):
   model = Menu
   template_name = "recipe/menu_update_form.html"
   form_class = MenuUpdateForm

class MenuDelete(LoginRequiredMixin, DeleteView):
    model = Menu
    template_name = "recipe/menu_delete_form.html"
    success_url = "/menu/list"

class PurchasedList(LoginRequiredMixin, ListView):
   model = Purchased

# Add your class below:
class PurchasedCreate(LoginRequiredMixin, CreateView):
  model = Purchased
  template_name = "recipe/purchased_create_form.html"
  form_class = PurchasedCreateForm

class PurchasedUpdate(LoginRequiredMixin, UpdateView):
   model = Purchased
   template_name = "recipe/purchased_update_form.html"
   form_class = PurchasedUpdateForm

class PurchasedDelete(LoginRequiredMixin, DeleteView):
    model = Purchased
    template_name = "recipe/purchased_delete_form.html"
    success_url = "/purchased/list"