from django.forms import ModelForm, Textarea

from .models import Wisdom


class WisdomForm(ModelForm):
    class Meta:
        model = Wisdom
        fields = ('words_of_wisdom', 'wisdom_origin',)
        widgets = {
            'words_of_wisdom': Textarea(attrs={'cols': 80, 'rows': 2, 'class': 'form-control'}),
            'wisdom_origin': Textarea(attrs={'cols': 80, 'rows': 2, 'class': 'form-control'}),
        }
