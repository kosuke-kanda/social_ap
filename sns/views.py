from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import PostForm
from .models import Post, User


# トップページ
class TopView(TemplateView):
    template_name = "top.html"

# タイムライン
class TimeLineView(ListView):
    template_name = "post_list.html"
    model = Post

# マイページ
class UserPageView(LoginRequiredMixin, ListView):
    template_name = "post_user_page.html"
    model = Post
    login_url = reverse_lazy('accounts:login')

    def get(self, request, user):
        try:
            selected_user = User.objects.get(username=user)
        except User.DoesNotExist:
            selected_user = None
        
        object_list = Post.objects.filter(username=selected_user).order_by("updated_at")
        context = {"selected_user": selected_user, "object_list": object_list}
        return render(request, "post_user_page.html", context)
    
# 投稿作成
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_form.html"
    success_url = reverse_lazy('sns:list')
    login_url = reverse_lazy('accounts:login')

    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        username = request.user
        text = request.POST["text"]
        Post.objects.create(username=username, text=text)
        messages.success(request, "新規投稿を作成しました！")
        return redirect("sns:list")
        
# 投稿削除
class DeltePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("sns:list") #TODO:削除完了後パラメータ取得してマイページに戻す 
    login_url = reverse_lazy('accounts:login')

    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        messages.success(request, "投稿を削除しました！")
        return super().post(request, *args, **kwargs)

    # def get_url_success(self):
    #     return reverse_lazy("sns:userPage",kwargs={"username":self.kwargs["username"]} )

    
        

