from django.urls import path
from .views import alta_abonado

urlpatterns = [
    path('alta/', alta_abonado, name='alta_abonado'),
]