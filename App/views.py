from django.shortcuts import render
from django.views.generic import ListView, DetailView

from App.models import Post
# Create your views here.
def index(request):
    return render(request,'index.html')

class PostList(ListView):
    model = Post
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

