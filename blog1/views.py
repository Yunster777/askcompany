from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    context = {
        'post_list': qs,
    }
    return render(request, 'blog1/post_list.html', context)
