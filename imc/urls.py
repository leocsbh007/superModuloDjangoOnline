from django.urls import path
from imc.views import calcula_imc


urlpatterns = [
    #path('', index, name='index'),
    path('calcula_imc', calcula_imc, name='calcula_imc'),

]