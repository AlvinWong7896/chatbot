from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is my first url")


def specific(request):
    return HttpResponse("This is the specific url")


def article(request, article_id):
    return render(request, "blog/index.html", {"article_id": article_id})
