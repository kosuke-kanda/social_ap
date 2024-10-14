from django.shortcuts import render


def top_view(request):
    return render(request, "sns/top.html")
