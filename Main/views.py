from django.shortcuts import render


def index(request):
    return render(request, "home/home.html")


def profile(request):
    return render(request, "profile/profile.html")


def collection(request):
    return render(request, "collection/collection.html")