from django.shortcuts import render, HttpResponse
from .component import renderPlus

# Create your views here.
def demo(request):
    return renderPlus(request, render(request, 'base.html'))


