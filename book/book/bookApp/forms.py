from django.forms import ModelForm
from .models import Rroduct

class RroductFrom(ModelForm):
    class Meta:
        model = Rroduct
        fields = ("title", 'price', "content", "rubric")