from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 1)  # 10 постов на странице
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_posts': page_posts})
