from django.shortcuts import render
from datetime import datetime
from .forms import SubscriberForm

# Create your views here.
def landing(request):

    now = datetime.now()
    name = 'Serge'
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        print(data['name'], data['email'])

        saved_form = form.save()

    return render(request, 'landing/index.html', locals())