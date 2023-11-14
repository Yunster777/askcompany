from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
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


post_list = ListView.as_view(
    model=Post,
    paginate_by=10,
)


# def generate_view_fn(model):
#     def view_fn(request, pk):
#         instance = get_object_or_404(model, pk=pk)
#         instance_name = model._meta.model_name
#         template_name = '{}/{}_detail.html'.format(model._meta.app_label,
#                                                    instance_name)
#         return render(request, template_name, {
#             instance_name: instance,
#         })
#     return view_fn
#
#
# post_detail = generate_view_fn(Post)


class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)

        return qs


post_detail = PostDetailView.as_view()

# post_detail = DetailView.as_view(
#     model=Post,
#     # queryset=Post.objects.filter(is_public=True),
# )


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     # post = Post.objects.get(pk=pk)
#     post = get_object_or_404(Post, pk=pk)
#     context = {
#         'post': post,
#     }
#     return render(request, 'instagram/post_detail.html', context)


def archives_year(request: HttpRequest, year: int) -> HttpResponse:
    return HttpResponse(f'{year}년 archives')
