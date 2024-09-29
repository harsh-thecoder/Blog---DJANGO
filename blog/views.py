from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post 
from django.views.generic import (
   ListView,
   DetailView,
   CreateView,
   UpdateView,
   DeleteView
)

def home(request):
     context = {
        'posts': Post.objects.all()
     }
      # First command will be request and second one will be the template we want to access in home
     return render(request,'blog/home.html',context) 

class PostListView(ListView):
   model = Post
   template_name = 'blog/home.html' #Format -> <app>/<model>_<viewtype>.html
   context_object_name = 'posts'
   ordering = ['-date_posted'] #To get the Latest post at the top 
   paginate_by = 6

class UserPostListView(ListView):
   model = Post
   template_name = 'blog/user_posts.html' #Format -> <app>/<model>_<viewtype>.html
   context_object_name = 'posts'
   ordering = ['-date_posted'] #To get the Latest post at the top 
   paginate_by = 6   

   def get_queryset(self):
      user = get_object_or_404(User, username = self.kwargs.get('username'))
      return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
   model = Post
   


class PostCreateView(LoginRequiredMixin, CreateView):
   model = Post
   fields = ['title','content']

   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form) 

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
   model = Post
   fields = ['title','content']

   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)       

   def test_func(self):
      post = self.get_object()
      if self.request.user == post.author:
          return True
      return False       

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Post     
   success_url = '/' #To go back to home page after deletion

   def test_func(self):
      post = self.get_object()
      if self.request.user == post.author:
          return True
      return False   

def about(request):
    return render(request,'blog/about.html',{'title' : 'About'}) #There is optional 3rd argument which we have not written as it's optional above we have entered that as context  
