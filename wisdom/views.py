from django.shortcuts import render
from .models import Wisdom


def random_wisdom(request):
    random_wisdom = Wisdom.objects.order_by('?').first()
    return render(request, 'home.html', {'random_wisdom': random_wisdom})
