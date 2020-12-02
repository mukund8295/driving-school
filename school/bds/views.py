from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django import template




def index(request):
    return render(request, 'index.html')