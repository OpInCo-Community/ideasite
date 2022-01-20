from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def profile(request):
    messages.add_message(request, messages.INFO, 'This feature is not available yet')

    return redirect("ideas:home")