from django.shortcuts import render

from .models import Wisdom


def random_wisdom(request):
    some_random_wisdom = Wisdom.objects.order_by('?').first()
    return render(request, 'home.html', {'wisdom': some_random_wisdom})


def wisdom_by_id(request, wisdom_id):
    wisdom = Wisdom.objects.filter(id=wisdom_id).first()
    if not wisdom:
        return random_wisdom(request)
    return render(request, 'home.html', {'wisdom': wisdom})
