from django import forms
from django.db.models import fields
from CardMakerApp.models import Carta

class CardModel2Form(forms.ModelForm):
    class Meta:
        model = Carta
        fields = ['nome','poder','raca','efeito','tipo','classe']


