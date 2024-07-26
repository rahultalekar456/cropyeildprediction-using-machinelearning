# agriculture/forms.py
from django import forms

class CropRecommendationForm(forms.Form):
    Nitrogen = forms.CharField(label="Enter Nitrogen")
    Phosphorous = forms.CharField(label="Enter Phosphorous")
    Potassium = forms.CharField(label="Enter Potassium")
    temperature = forms.CharField(label="Enter temperature")
    humidity = forms.CharField(label="Enter humidity")
    ph = forms.CharField(label="Enter ph")
    rainfall = forms.CharField(label="Enter rainfall")
