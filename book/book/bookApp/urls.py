from django.urls import path
from django.views.generic import TemplateView
from .views import TwoModelsView

urlpatterns = [
    path("", TemplateView.as_view(template_name="main.html"), name="main"),
    path("prod/", TwoModelsView.as_view(), name="prod")
]