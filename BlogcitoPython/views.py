from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from BlogcitoPython.models import Post
from BlogcitoPython.forms import UserForm

def index(request):
    return render(request, 'BlogcitoPython/index.html', {})

class PostList(ListView):
    model = Post

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy('blogcitopython_listar')
    fields = '__all__'

class DetailPost(DetailView):
    model = Post

class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blogcitopython_listar')

class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('blogcitopython_listar')
    fields = '__all__'

class UserSignUp(CreateView):
    form_class = UserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('blogcitopython_listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('blogcitopython_listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('blogcitopython_listar')