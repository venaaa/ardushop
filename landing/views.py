from django.shortcuts import render
from datetime import datetime

# Create your views here.
def landing(request):

    now = datetime.now()
    name = 'Serge'
    return render(request, 'landing/index.html', locals())