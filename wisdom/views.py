from django.shortcuts import render, redirect
from .models import Wisdom
from .forms import WisdomForm


def random_wisdom(request):
    some_random_wisdom = Wisdom.objects.filter(is_public=True).order_by('?').first()
    return render(request, 'home.html', {'wisdom': some_random_wisdom})


def wisdom_by_id(request, wisdom_id):
    wisdom = Wisdom.objects.filter(id=wisdom_id, is_public=True).first()
    if not wisdom:
        return redirect('/')
    return render(request, 'home.html', {'wisdom': wisdom})


def post_new_wisdom(request):
    if request.method == "POST":
        form = WisdomForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')
    else:
        form = WisdomForm()
    return render(request, 'addWisdom.html', {'form': form})


def wisdoms(request):
    wisdoms = Wisdom.objects.filter(is_public=True)
    if not wisdoms:
        return redirect('/')
    return render(request, 'wisdoms.html', {'wisdoms': wisdoms})
