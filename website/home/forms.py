from django import forms
from .models import *

class symptomsForm(forms.ModelForm):

    class Meta:
        model = symptoms
        fields = ('age', 'restbp','chol','gender','durationexercise','maxHeartRate')

class diabSympForm(forms.ModelForm):

    class Meta:
        model = diabSymp
        fields = ('insulinDose', 'prebreakfastglucose','postbreakfastglucose','exerciseactivity','specialEvent')


