from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd

from myapp.forms import *
from myapp.models import *

from .forms import *
from .models import *

# Load your model at the beginning (assuming it's in the root of your project)
MODEL_PATH = r'model/agriculture/crop_recommeddation.pickle'
model = pd.read_pickle(MODEL_PATH)

@login_required
def crop_recommendation(request):
    users_count = User.objects.all().count()
    consumers = Consumer.objects.all().count
    review_count = Review.objects.all().count()

    
    crop_details = {
        'rice': {
            'nitrogen': 'High',
            'phosphorous': 'Medium',
            'potassium': 'High',
            'temperature': '25-30°C',
            'humidity': '70-90%',
            'ph': '5.5-7.0',
            'rainfall': '1000-1500 mm',
            'reason': 'Rice requires a lot of water and nutrients, which is why it is best suited for areas with high rainfall and fertile soil.'
        },
        'wheat': {
            'nitrogen': 'Medium',
            'phosphorous': 'High',
            'potassium': 'Medium',
            'temperature': '15-25°C',
            'humidity': '50-70%',
            'ph': '6.0-7.5',
            'rainfall': '500-700 mm',
            'reason': 'Wheat is a hardy crop that can tolerate a wide range of conditions, but it prefers well-drained soil and moderate temperatures.'
        },
        'maize': {
            'nitrogen': 'High',
            'phosphorous': 'Medium',
            'potassium': 'High',
            'temperature': '20-25°C',
            'humidity': '60-80%',
            'ph': '5.5-7.0',
            'rainfall': '700-1000 mm',
            'reason': 'Maize is a tall crop that requires a lot of sunlight, so it is best suited for areas with long growing seasons and fertile soil.'
        },
        'chickpea': {
            'nitrogen': 'Medium',
            'phosphorous': 'Low',
            'potassium': 'Medium',
            'temperature': '15-20°C',
            'humidity': '40-60%',
            'ph': '7.0-8.5',
            'rainfall': '400-600 mm',
            'reason': 'Chickpea is a drought-tolerant crop that can grow in poor soil conditions, making it a good choice for areas with limited water resources.'
        },
        'kidney beans': {
            'nitrogen': 'Medium',
            'phosphorous': 'Medium',
            'potassium': 'High',
            'temperature': '20-25°C',
            'humidity': '60-80%',
            'ph': '6.0-7.0',
            'rainfall': '700-1000 mm',
            'reason': 'Kidney beans are a versatile crop that can be grown in a variety of climates, but they prefer well-drained soil and moderate temperatures.'
        },
        'pigeon peas': {
            'nitrogen': 'Medium',
            'phosphorous': 'Low',
            'potassium': 'Medium',
            'temperature': '20-25°C',
            'humidity': '60-80%',
            'ph': '6.5-7.5',
            'rainfall': '500-700 mm',
            'reason': 'Pigeon peas are a drought-tolerant crop that can grow in poor soil conditions, making it a good choice for areas with limited water resources.'
        },
        'moth beans': {
            'nitrogen': 'Medium',
            'phosphorous': 'Low',
            'potassium': 'Medium',
            'temperature': '20-25°C',
            'humidity': '60-80%',
            'ph': '6.0-7.0',
            'rainfall': '500-700 mm',
            'reason': 'Moth beans are a drought-tolerant crop that can grow in poor soil conditions, making it a good choice for areas with limited water resources.'
        },
        'mung bean': {
            'nitrogen': 'Medium',
            'phosphorous': 'Medium',
            'potassium': 'High',
            'temperature': '20-25°C',
            'humidity': '60-80%',
            'ph': '6.0-7.0',
            'rainfall': '500-700 mm',
            'reason': 'Mung beans are a versatile crop that can be grown in a variety of climates, but they prefer well-drained soil and moderate temperatures.'
        },
        'black gram': {
            'nitrogen': 'Medium',
            'phosphorous': 'Medium',
            'potassium': 'High',
            'temperature': '20-25°C',
            'humidity': '60-80%',
            'ph': '6.0-7.0',
            'rainfall': '500-700 mm',
            'reason': 'Black gram is a versatile crop that can be grown in a variety of climates, but they prefer well-drained soil and moderate temperatures.'
        },
        'lentil': {
            'nitrogen': 'Medium',
            'phosphorous': 'Low',
            'potassium': 'Medium',
            'temperature': '15-20°C',
            'humidity': '40-60%',
            'ph': '7.0-8.5',
            'rainfall': '400-600 mm',
            'reason': 'Lentil is a drought-tolerant crop that can grow in poor soil conditions, making it a good choice for areas with limited water resources.'
        },
        'pomegranate': {
            'nitrogen': 'Medium',
            'phosphorous': 'High',
            'potassium': 'High',
            'temperature': '15-25°C',
            'humidity': '50-70%',
            'ph': '6.0-7.5',
            'rainfall': '500-700 mm',
            'reason': 'Pomegranate is a hardy crop that can tolerate a wide range of conditions, but it prefers well-drained soil and moderate temperatures.'
        },
        'banana': {
            'nitrogen': 'High',
            'phosphorous': 'Medium',
            'potassium': 'High',
            'temperature': '25-30°C',
            'humidity': '70-90%',
            'ph': '5.5-7.0',
            'rainfall': '1000-1500 mm',
            'reason': 'Banana is a tropical crop that requires a lot of water and nutrients, which is why it is best suited for areas with high rainfall and fertile soil.'
        },
        'mango': {
            'nitrogen': 'Medium',
            'phosphorous': 'High',
            'potassium': 'Medium',
            'temperature': '20-25°C',
            'humidity': '60-80%',
            'ph': '5.5-7.0',
            'rainfall': '700-1000 mm',
            'reason': 'Mango is a tropical crop that requires a lot of sunlight, so it is best suited for areas with long growing seasons and fertile soil.'
        },
        'grapes': {
            'nitrogen': 'Medium',
            'phosphorous': 'Medium',
            'potassium': 'High',
            'temperature': '15-25°C',
            'humidity': '50-70%',
            'ph': '6.0-7.5',
            'rainfall': '500-700 mm',
            'reason': 'Grapes are a hardy crop that can tolerate a wide range of conditions, but they prefer well-drained soil and moderate temperatures.'
        },
        'apple': {
            'nitrogen': 'Medium',
            'phosphorous': 'Medium',
            'potassium': 'High',
            'temperature': '10-15°C',
            'humidity': '50-70%',
            'ph': '6.0-7.5',
            'rainfall': '500-700 mm',
            'reason': 'Apple is a temperate crop that requires a cold winter and a warm summer, so it is best suited for areas with a continental climate.'
        },
        'orange': {
            'nitrogen': 'Medium',
            'phosphorous': 'High',
            'potassium': 'High',
            'temperature': '20-25°C',
            'humidity': '60-80%',
            'ph': '5.5-7.0',
            'rainfall': '700-1000 mm',
            'reason': 'Orange is a tropical crop that requires a lot of sunlight, so it is best suited for areas with long growing seasons and fertile soil.'
        }
    } 

    if request.method == "POST":
        form = CropRecommendationForm(request.POST)
        if form.is_valid():
            # Prepare data for prediction
            data = [form.cleaned_data[i] for i in ['Nitrogen', 'Phosphorous', 'Potassium', 'temperature', 'humidity', 'ph', 'rainfall']]
            prediction = model.predict([data])

            # Send prediction and input data to template
            context = {
                'users_count':users_count,
                'consumers':consumers,
                'review_count':review_count,
                'prediction': prediction[0],
                'input_data': {
                    'Nitrogen': form.cleaned_data['Nitrogen'],
                    'Phosphorous': form.cleaned_data['Phosphorous'],
                    'Potassium': form.cleaned_data['Potassium'],
                    'temperature': form.cleaned_data['temperature'],
                    'humidity': form.cleaned_data['humidity'],
                    'ph': form.cleaned_data['ph'],
                    'rainfall': form.cleaned_data['rainfall'],
                },
                'crop_details': crop_details.get(prediction[0].lower(), {})  # Get crop details based on prediction
            }
            return render(request, 'dashboard/dashboard.html', context)
    else:
        form = CropRecommendationForm()
    return render(request, 'predict.html', {'form': form})


from django.shortcuts import render

def schemes(request):
    schemes_data = [
        {
            "name": "PM Kisan Samman Nidhi",
            "type": "Central Government Scheme",
            "eligibility": "Small and marginal farmers",
            "details": "Provides income support of ₹6,000 per year to eligible farmers, payable in three equal installments."
        },
        {
            "name": "Rashtriya Krishi Vikas Yojana (RKVY)",
            "type": "Central Government Scheme",
            "eligibility": "Farmers, Farmer Groups/Cooperatives, Farmer Producer Organizations (FPOs), etc.",
            "details": "Aims to strengthen agriculture by providing financial assistance for various activities such as production, post-harvest management, infrastructure, etc."
        },
        {
            "name": "Pradhan Mantri Fasal Bima Yojana (PMFBY)",
            "type": "Central Government Scheme",
            "eligibility": "All farmers including sharecroppers and tenant farmers",
            "details": "Provides insurance coverage and financial support to farmers in case of crop loss due to natural calamities, pests, diseases, etc."
        },
        {
            "name": "Kisan Credit Card (KCC) Scheme",
            "type": "Central Government Scheme",
            "eligibility": "Farmers",
            "details": "Provides short-term credit to farmers for their agricultural and allied activities at affordable interest rates."
        },
        {
            "name": "Rythu Bandhu Scheme",
            "type": "State Government Scheme",
            "eligibility": "Farmers holding cultivable land",
            "details": "Offers financial assistance to farmers in the form of investment support before the sowing season to meet their farm input costs."
        },
        {
            "name": "Rythu Bima Scheme",
            "type": "State Government Scheme",
            "eligibility": "Farmers",
            "details": "Provides life insurance coverage to farmers and their families in case of death or disability."
        }
        # Add more schemes as needed...
    ]

    return render(request, 'schemes.html', {'schemes': schemes_data})
