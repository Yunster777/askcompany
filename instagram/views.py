from IPython.utils._sysinfo import commit
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    ListView,
    ArchiveIndexView,
    YearArchiveView,
    MonthArchiveView,
    DayArchiveView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from .models import Post
from .forms import PostForm


# post list
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 15
    # ordering = ['created_at']


post_list = PostListView.as_view()


# post detail
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)

        return qs


post_detail = PostDetailView.as_view()


# create post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, "포스팅을 성공적으로 저장했습니다.")
        return super().form_valid(form)


post_new = PostCreateView.as_view()


# update post
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, "포스팅을 성공적으로 수정했습니다.")
        return super().form_valid(form)


post_edit = PostUpdateView.as_view()


# delete post
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # reverse_lazy 는 코드 수행될때 말고 값이 사용될 때 reverse 해줌
    success_url = reverse_lazy("instagram:post_list")

    # 이렇게 쓰면 서버에서 오류남. 프로젝트를 로딩하기 전에 이 코드가 실행되기 때문
    # 프로젝트를 로딩해야만 reverse 사전이 생성됨
    # success_url = reverse("instagram:post_list")

    # 이것도 좀 불편한 방법
    def get_success_url(self):
        return reverse("instagram:post_list")


post_delete = PostDeleteView.as_view()


post_archive = ArchiveIndexView.as_view(
    model=Post, date_field="created_at", paginate_by=10
)

post_archive_year = YearArchiveView.as_view(
    model=Post, date_field="created_at", make_object_list=True
)

post_archive_month = MonthArchiveView.as_view(
    model=Post, date_field="created_at", month_format="%m"
)

post_archive_day = DayArchiveView.as_view(
    model=Post, date_field="created_at", month_format="%m"
)


# 여기부터는 공부하면서 짠 코드들 #

# @login_required
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


# @login_required
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # form 의 값 외에도 다른 값이 들어가서 저장해야 할 경우 commit False 사용
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             messages.success(request, "포스팅을 성공적으로 저장했습니다.")
#             return redirect(post)
#     else:
#         form = PostForm()
#
#     context = {
#         "form": form,
#         "post": None,
#     }
#
#     return render(request, "instagram/post_form.html", context)


# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if post.author != request.user:
#         messages.error(request, "작성자만 수정할 수 있습니다.")
#         return redirect(post)
#
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             messages.success(request, "포스팅을 성공적으로 저장했습니다.")
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)
#
#     context = {
#         "form": form,
#         "post": post,
#     }
#
#     return render(request, "instagram/post_form.html", context)


# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if post.author != request.user:
#         messages.error(request, "작성자만 삭제할 수 있습니다.")
#         return redirect(post)
#
#     if request.method == "POST":
#         post.delete()
#         messages.success(request, "포스팅을 삭제했습니다.")
#         return redirect("instagram:post_list")
#
#     context = {
#         "post": post,
#     }
#
#     return render(request, "instagram/post_confirm_delete.html", context)


# post_list = ListView.as_view(
#     model=Post,
#     paginate_by=10,
# )


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


# def archives_year(request: HttpRequest, year: int) -> HttpResponse:
#     return HttpResponse(f'{year}년 archives')
