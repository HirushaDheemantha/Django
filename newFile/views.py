from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def new_view(request):
    return HttpResponse("This is the newFile app!")