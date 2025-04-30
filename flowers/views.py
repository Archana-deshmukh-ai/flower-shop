from django.shortcuts import render, get_object_or_404
from flowers.models import Flower  

def search_flowers(request):
    query = request.GET.get('q')
    results = Flower.objects.filter(name__icontains=query)
    return render(request, 'flowers/search_results.html', {'results': results, 'query': query})


def budget_view(request):
    flowers = Flower.objects.all()
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price and max_price:
        flowers = flowers.filter(price__gte=min_price, price__lte=max_price)

    return render(request, 'flowers/budget.html', {'flowers': flowers})

def flower_detail(request, id):
    flower = get_object_or_404(Flower, id=id)
    description_lines = flower.description.splitlines()
    return render(request, 'flowers/detail.html', {'flower': flower, 'description_lines': description_lines})

def bestsellers(request):
    flowers = Flower.objects.filter(is_bestseller=True)
    return render(request, 'flowers/list.html', {'flowers': flowers, 'title': 'Bestsellers'})

def seasonal(request):
    flowers = Flower.objects.filter(is_seasonal=True)
    return render(request, 'flowers/list.html', {'flowers': flowers, 'title': 'Seasonal Flowers'})

def new_flowers(request):
    flowers = Flower.objects.filter(is_new=True)
    return render(request, 'flowers/list.html', {'flowers': flowers, 'title': 'New Arrivals'})


