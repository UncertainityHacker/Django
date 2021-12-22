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

    features = Feature.objects.all()

    return render(request, 'index.html', {'features': features})