from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User
from BlogcitoPython.models import Post, Avatar, Message
from BlogcitoPython.forms import UserForm

def index(request):
    posts = Post.objects.order_by('-publish_date').all()
    return render(request, 'BlogcitoPython/index.html', {'posts': posts})

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

class UpdateAvatar(LoginRequiredMixin, UpdateView):
    model = Avatar
    fields = ['image']
    success_url = reverse_lazy('blogcitopython_listar')

class UpdateUser(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('blogcitopython_listar')

class DetailMessage(LoginRequiredMixin, DetailView):
    model = Message

class MessageList(LoginRequiredMixin, ListView):
    model = Message

class CreateMessage(CreateView):
    model = Message
    success_url = reverse_lazy('blogcitopython_crear_mensajes')
    fields = ['name', 'email', 'text']

class DeleteMessage(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('blogcitopython_listar_mensajes')

def about(request):
    return render(request, 'BlogcitoPython/about.html')