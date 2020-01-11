from django.shortcuts import render
from birdy.twitter import UserClient


def twitter_war(request):
    client = UserClient('5xOlVgTTxqlDp3c9NbhDxypXC',
                        'rXFB2WgX3rLQ3S0PPYOI2b6UA3sKMwF7VZpTQA03jCasDzPOt2',
                        '2982752483-A6yeIrm7qC4QHPL3Ar0Hphvg2bZHqHAnJ62f7sr',
                        'o8qR72i1tiampZnWtlZOuZq97tyEBynNk75U9BhH5X2r3')

    twitter_names = ['brunoraljic', 'EnsarBavrk', "Ognjetina", "sdejan89", "_rstokic_",
                     "milansusnjar_", "KnightOfRen_", "A_Popadic", "milos_brdar", "borisjanjanin",
                     "deni_n88", "djovic82", "GJungic", "Gonguli88", "buconis", "ozegster", "mladen_vasic",
                     "Nemanjas_Vasic", "novislavs", "stek993", "Tin_M_", "stasa_m"]

    twitter_accounts = []

    for twitter_name in twitter_names:
        twitter_accounts.append(client.api.users.show.get(screen_name=twitter_name).data)

    twitter_accounts.sort(key=lambda x: x['followers_count'], reverse=True)

    return render(request, 'war.html', {"twitter_accounts": twitter_accounts[:10]})
