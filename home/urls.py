from django.urls import path
from .views import IndexView, SobreView, ProjetosView, OrcamentosView

urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('about/', SobreView.as_view(),name='about'),
    path('projects/', ProjetosView.as_view(),name='projects'),
    path('budget/', OrcamentosView.as_view(),name='budget'),
]