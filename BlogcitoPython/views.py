from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from BlogcitoPython.models import Post

def index(request):
    return render(request, 'BlogcitoPython/index.html', {})

class PostList(ListView):
    model = Post

class CreatePost(CreateView):
    model = Post
    success_url = reverse_lazy('blogcitopython_listar')
    fields = '__all__'

class DetailPost(DetailView):
    model = Post

class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('blogcitopython_listar')

class UpdatePost(UpdateView):
    model = Post
    success_url = reverse_lazy('blogcitopython_listar')
    fields = '__all__'