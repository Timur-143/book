from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Rroduct, Rubric
from .forms import RroductFrom

class TwoModelsView(ListView):
    model = Rroduct
    context_object_name = "products"
    template_name = "prod.html"

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data()
    #     context['rubric'] = Rubric.objects.all()
    #     return context