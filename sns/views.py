from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView

from .forms import PostForm
from .models import Post, User


# トップページ
class TopView(TemplateView):
    template_name = "top.html"

# タイムライン
class TimeLineView(ListView):
    template_name = "post_list.html"
    model = Post

# 投稿作成
class CreatePostView(CreateView):
        model = Post
        form_class = PostForm
        template_name = "post_form.html"
        success_url = reverse_lazy('sns:list')

        # 投稿ボタン
        def post(self, request: HttpRequest, *args: str, **kwargs: reverse_lazy) -> HttpResponse:
            username = request.user
            text = request.POST["text"]
            Post.objects.create(username=username, text=text)
            return redirect("sns:list")
