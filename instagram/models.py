from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    # 이미지 필드 쓰게 되면 필히 pillow 라이브러리 설치
    photo = models.ImageField(blank=True, upload_to="instagram/post/%Y/%m/%d")
    tag_set = models.ManyToManyField("Tag", blank=True)
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    # 모델을 작성하면 필히 get_absolute_url 작성하기
    # url reverse 편하게 사용하기 위해
    # python: resolve_url(post), redirect(post)
    # html: {{ post.get_absolute_url }}
    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("instagram:post_detail", args=[self.pk])

    class Meta:
        ordering = ["-id"]

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = '메세지 글자수'


class Comment(models.Model):
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, limit_choices_to={"is_public": True}
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name} ({self.id})"

    # post_set = models.ManyToManyField('Post')
