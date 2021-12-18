from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
# def index(request):
#     name = 'Rick'
#     context = {
#         'name':'Rick',
#         'age': 23,
#         'nationality':'Indian'
#     }
#     # return render(request, 'index.html', {'name':name})
#     return render(request, 'index.html', context)

# def counter(request):
#     text = request.POST['text']
#     amount_of_words = len(text.split())
#     return render(request, 'counter.html', {'amount':amount_of_words})

# Dynamic data test function

def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Basic Fitness'
    feature1.details = 'Getting fit has now become very easy!'
    feature1.is_true = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'New Gym Training'
    feature2.details = 'Getting fit has now become very easy!'
    feature2.is_true = False

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Basic Muscle Course'
    feature3.details = 'Getting fit has now become very easy!'
    feature3.is_true = False
    
    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Advanced Muscle Course'
    feature4.details = 'Getting fit has now become very easy!'
    feature4.is_true = False

    feature5 = Feature()
    feature5.id = 4
    feature5.name = 'Yoga Training'
    feature5.details = 'Getting fit has now become very easy!'
    feature5.is_true = True

    feature6 = Feature()
    feature6.id = 5
    feature6.name = 'Body Building Course'
    feature6.details = 'Getting fit has now become very easy!'
    feature6.is_true = False

    featuresleft = [feature1, feature2, feature3]
    featuresright = [feature4, feature5, feature6]

    return render(request, 'index.html', {'featuresleft': featuresleft, 'featuresright': featuresright})