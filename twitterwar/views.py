from django.shortcuts import render
from birdy.twitter import UserClient


def twitter_war(request):
    client = UserClient('5xOlVgTTxqlDp3c9NbhDxypXC',
                        'rXFB2WgX3rLQ3S0PPYOI2b6UA3sKMwF7VZpTQA03jCasDzPOt2',
                        '2982752483-A6yeIrm7qC4QHPL3Ar0Hphvg2bZHqHAnJ62f7sr',
                        'o8qR72i1tiampZnWtlZOuZq97tyEBynNk75U9BhH5X2r3')

    bruno = client.api.users.show.get(screen_name='brunoraljic')
    enso = client.api.users.show.get(screen_name='EnsarBavrk')

    return render(request, 'war.html',
                  {"bruno_followers": bruno.data['followers_count'], "enso_followers": enso.data['followers_count'],
                   'bruno_image': bruno.data['profile_image_url'], 'enso_image': enso.data['profile_image_url']})
