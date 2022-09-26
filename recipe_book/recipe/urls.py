from django.urls import path, include
from . import views

urlpatterns = [path('', views.home, name="home"),
path("accounts/", include("django.contrib.auth.urls"), name="login"),
path("logout/", views.logout_view, name="logout"),
path('ingredients/list/', views.IngredientsList.as_view(), name="ingredientslist"),
path('ingredients/create/', views.IngredientsCreate.as_view(), name="ingredientscreate"),
path('ingredients/update/<pk>/', views.IngredientsUpdate.as_view(), name="ingredientsupdate"),
path('ingredients/delete/<pk>/', views.IngredientsDelete.as_view(), name="ingredientsdelete"),
path('menu/list/', views.MenuList.as_view(), name="menulist"),
path('menu/create/', views.MenuCreate.as_view(), name="menucreate"),
path('menu/update/<pk>/', views.MenuUpdate.as_view(), name="menuupdate"),
path('menu/delete/<pk>/', views.MenuDelete.as_view(), name="menudelete"),
path('purchased/list/', views.PurchasedList.as_view(), name="purchasedlist"),
path('purchased/create/', views.PurchasedCreate.as_view(), name="purchasedcreate"),
path('purchased/update/<pk>/', views.PurchasedUpdate.as_view(), name="purchasedupdate"),
path('purchased/delete/<pk>/', views.PurchasedDelete.as_view(), name="purchaseddelete"),
path("signup/", views.SignUp.as_view(), name="signup"),
] 