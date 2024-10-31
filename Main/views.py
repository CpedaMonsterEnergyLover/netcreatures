from django.shortcuts import render
from django.contrib.auth.models import User
from .auth import extract_token, get_token_email
from django.http import JsonResponse
from rest_framework.views import APIView


def index(request):
    return render(request, "home/home.html")


def profile(request):
    return render(request, "profile/profile.html")


def collection(request):
    return render(request, "collection/collection.html")


class LinkAccount(APIView):

    def post(self, request):
        token = extract_token(request)
        email = get_token_email(token)

        user = User.objects.get(email=email)
        latest_user = User.objects.order_by('-id').first()
        next_id = latest_user.id + 1 if latest_user is not None else 1

        if user:
            return JsonResponse(data={
                'status': 'ok',
                'created': False
            }, safe=False)

        user = User(
            username=f"NetStalker{next_id}",
            email=email
        )
        user.save()

        return JsonResponse(data={
            'status': 'ok',
            'created': True
        }, safe=False)
