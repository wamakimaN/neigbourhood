from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .models import  Profile, Post, Business, Neighborhood

# Create your views here.

def registration(request):
  form = UserCreationForm()

  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()

  context = {'form':form}
  return render(request, 'signup.html', context)