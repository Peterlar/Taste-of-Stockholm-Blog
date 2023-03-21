from django.shortcuts import render
from django.views import generic
from .models import Post




class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


def index(request):
    return render(request, 'index.html', {})


def ag(request):
    return render(request, 'ag.html', {})


def spesso(request):
    return render(request, 'spesso.html', {})