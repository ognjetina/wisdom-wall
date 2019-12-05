from django.shortcuts import render, redirect
from .models import Wisdom, Toxicity
from .forms import WisdomForm
from django.http import JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt


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
    wisdoms = Wisdom.objects.filter(is_public=True).order_by('-wisdom_occurrence_time')
    if not wisdoms:
        return redirect('/')
    return render(request, 'wisdoms.html', {'wisdoms': wisdoms})

@csrf_exempt
def toxicity(request):
    if request.method == "POST":
        print('here')
        # increment toxicity lvl
        toxicity = Toxicity.objects.filter(created=datetime.date.today()).first()
        toxicity.level = toxicity.level + 1
        toxicity.save()
        if toxicity:
            return JsonResponse({'toxicity': toxicity.level})
        else:
            new_toxicity = Toxicity()
            new_toxicity.save()
            return JsonResponse({'toxicity': new_toxicity.level})

    elif request.method == "GET":
        # get toxicity lvl
        toxicity = Toxicity.objects.filter(created=datetime.date.today()).first()
        if toxicity:
            return JsonResponse({'toxicity': toxicity.level})
        else:
            new_toxicity = Toxicity()
            new_toxicity.save()
            return JsonResponse({'toxicity': new_toxicity.level})


def view_404(request, *args, **argv):
    return redirect('/')
