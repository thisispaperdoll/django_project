from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView


class PostCreate(CreateView):
    model = Post 
    fields = ["title", "content", "head_image", "tag"]

class PostDetail(DetailView):
    model = Post 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = '임의로 작성한 새로운 변수'
        print(context["now"] )
        return context

class PostList(ListView):   # post_list.html, post-list
    model = Post 
    # template_name = 'blog/index.html' 
    ordering = '-pk' 
    context_object_name = 'post_list'

def index(request): # 함수를 만들고, 그 함수를 도메인 주소 뒤에 달아서 호출하는 구조
    posts = Post.objects.all()
    return render(
        request,
        'blog/index.html', {
            'posts':posts, 'my_list': ["apple", "banana", "cherry"], 'my_text': "첫번째 줄 \n 두번째 줄", 'content' : '<img src="data/jjangu.jpg" / >'
        }
    )# 없는 index.html을 호출하고 있음

def about_me(request): # 함수를 만들고, 그 함수를 도메인 주소 뒤에 달아서 호출하는 구조
    return render(
        request,
        'blog/about_me.html'
    )