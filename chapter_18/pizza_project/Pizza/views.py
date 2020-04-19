from django.shortcuts import render
from .models import Pizza
# Create your views here.
def index(request):
    return render(request, 'Pizza/index.html')

def pizzas(request):
    '''Show all pizzas'''
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'Pizza/pizzas.html', context)


def toppings(request, pizza_id):
    '''Show single topic and all its entries'''
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.entry_set.order_by('-pizzas')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'Pizza/toppings.html', context)
