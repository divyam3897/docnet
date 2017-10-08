from django.shortcuts import render
from .forms import *
from django.views.generic import TemplateView
import random

class Home(TemplateView):
    template_name = 'home.html'

def check_heartSymptom(request):
    form = symptomsForm()

    if request.method == 'POST': # If the form has been submitted...
        form = symptomsForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            print(request.POST)
            x = random.randint(0, 1)
            if(x == 0):
                return render(request,'heartWell.html',{'type':"Heart"})
            else:
                return render(request,'heartUnwell.html',{'type':"Heart"})

    else:
        return render(request, 'symptoms.html', {'form': form,'type':"Heart"})

def check_diabSymptom(request):
    form = diabSympForm()

    if request.method == 'POST': # If the form has been submitted...
        form = diabSympForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            print(request.POST)
            x = random.randint(0, 1)
            if(x == 0):
                return render(request,'heartWell.html',{'type':"Diabetes"})
            else:
                return render(request,'heartUnwell.html',{'type':"Diabetes"})

    else:
        return render(request, 'symptoms.html', {'form': form,'type':"Diabetes"})
