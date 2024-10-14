from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Post


class TopView(TemplateView):
    template_name = "top.html"

def list_view(request):
    object_list = Post.objects.all().order_by("updated_at")
    context = {"object_list": object_list}
    return render(request, "post_list.html", context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) 
    #     context["foo"] = "bar"
    #     return context

# def top_view(request):
#     return render(request, "sns/top.html")

