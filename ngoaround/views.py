from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Welcome to home page of our site")
    return render(request=request,template_name="ngoaround/index.html")