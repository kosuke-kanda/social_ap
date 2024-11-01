from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, logout
from django.views.generic import CreateView, ListView 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import LoginForm, SignUpForm
from django.http import HttpRequest, HttpResponse

from .forms import SignUpForm

# TODO:ユーザー切り替え機能を作る

# 新規ユーザー登録
class SignUpView(CreateView):
    model = User
    template_name = "signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("sns/top.html")

    def form_valid(self, form):
        user = form.save()
        # 登録した内容を元にログインする
        auth.login(self.request, user)
        # TODO: 成功時メッセージ出したい
        return redirect(("sns:top"))

# ログイン
class LoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy('sns:list')

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        messages.success(request, "ログインしました！")
        return super().post(request, *args, **kwargs)
    
# ログアウト
class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "logout.html"
    success_url = reverse_lazy('sns:top')
