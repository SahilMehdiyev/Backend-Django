from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def blogs(request):
    return render(request,'blog/blogs.html')

def blogs_details(request,id):
    return render(request,'blog/blog-details.html') 