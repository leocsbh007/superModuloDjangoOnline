from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from imc.forms import ImcForms


# Create your views here.
def calcula_imc(request):    
    form = ImcForms(request.POST)

    if form.is_valid():
        return render(request, 'imc/resultado.html')
    else: 
        form = ImcForms()
    return render(request, 'imc/index.html', {'form' : form})
    #return render(request, 'imc/index1.html')

