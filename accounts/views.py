from typing import Any
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, logout
from django.views.generic import CreateView, ListView 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import LoginForm, SignUpForm

from .forms import SignUpForm

# 新規ユーザー登録
class SignUpView(CreateView):
    template_name = "signup.html"

    model = User
    form_class = SignUpForm
    success_url = "sns/top.html"

    def form_valid(self, form):
        # Userテーブルに新規登録
        user = form.save()
        # 登録した内容を元にログインする
        auth.login(self.request, user)
        # 登録完了後、トップ画面にリダイレクトする
        return redirect(("sns:top"))


# class UserListView(ListView):
#     model = User
#     template_name = 'sns:top' #表示したいHTML
#     context_object_name = 'userResults' #好きな名前

# ログイン画面
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect("sns:list")
    else:
        form = LoginForm()
    param = {"form": form}
    return render(request, "login.html", param)

# ログアウト
def logout_view(request):
    logout(request)
    return render(request, "logout.html")