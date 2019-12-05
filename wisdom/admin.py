from django.contrib import admin
from .models import Wisdom, Toxicity


class WisdomAdmin(admin.ModelAdmin):
    list_display = ('is_public', 'words_of_wisdom')
    ordering = ('is_public',)


admin.site.register(Wisdom, WisdomAdmin)
admin.site.register(Toxicity)
