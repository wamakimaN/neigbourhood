from django.shortcuts import render,reverse,get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import  Profile, Post, Business, Neighborhood

# Create your views here.
def home_page(request):
    title = 'Welcome'
    return render(request, 'home.html', {"title": title})

@login_required
def profile(request):
    return render(request, 'profile.html')

def registration(request):
  form = UserCreationForm()

  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()

  context = {'form':form}
  return render(request, 'signup.html', context)

class PostHood(ListView):
  model = Post
  template_name = 'hood.html'

  def get_queryset(self):
    self.neighbor = get_object_or_404(Neighborhood,pk=self.kwargs['pk'])
    return Post.objects.filter(neighbor=self.neighbor)

  def get_context_data(self,**kwargs):
    context = super(PostHood, self).get_context_data(**kwargs)
    context['neighbor'] = self.neighbor
    return context