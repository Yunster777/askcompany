from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Post


# def post_list(request: HttpRequest) -> HttpResponse:
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#
#     if q:
#         qs = qs.filter(message__icontains=q)
#
#     context = {
#         'post_list': qs,
#         'q': q,
#     }
#
#     return render(request, 'instagram/post_list.html', context)


post_list = ListView.as_view(model=Post)


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    response = HttpResponse()
    response.write('Hello World!!</br >')
    response.write('Hello World!!</br >')
    response.write('Hello World!!</br >')
    return response
    # post = get_object_or_404(Post, id=pk)
    #
    # context = {
    #     'post': post,
    # }
    #
    # return render(request, 'instagram/post_detail.html', context)
