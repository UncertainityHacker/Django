from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = 'Rick'
    context = {
        'name':'Rick',
        'age': 23,
        'nationality':'Indian'
    }
    # return render(request, 'index.html', {'name':name})
    return render(request, 'index.html', context)