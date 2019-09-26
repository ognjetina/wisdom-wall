from django.shortcuts import render, redirect
from .models import Wisdom
from .forms import WisdomForm

from birdy.twitter import UserClient

def random_wisdom(request):
    client = UserClient('5xOlVgTTxqlDp3c9NbhDxypXC',
                        'rXFB2WgX3rLQ3S0PPYOI2b6UA3sKMwF7VZpTQA03jCasDzPOt2',
                        '2982752483-A6yeIrm7qC4QHPL3Ar0Hphvg2bZHqHAnJ62f7sr',
                        'o8qR72i1tiampZnWtlZOuZq97tyEBynNk75U9BhH5X2r3')

    bruno = client.api.users.show.get(screen_name='brunoraljic')
    enso = client.api.users.show.get(screen_name='mrFunkyWisdom')
    some_random_wisdom = Wisdom.objects.filter(is_public=True).order_by('?').first()
    return render(request, 'home.html', {'wisdom': some_random_wisdom,"bruno_followers":bruno.data['followers_count'],"enso_followers":enso.data['followers_count']})


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


def handle_404(request, *args, **argv):
    return redirect('/')
