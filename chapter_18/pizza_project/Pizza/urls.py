'''Defines URL pattern for learning_logs.'''

from django.urls import path
from . import views

app_name = 'Pizza'

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Show all pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    #Display toppings
    path('pizzas/<int:pizza_id>/', views.toppings, name='toppings'),

]
