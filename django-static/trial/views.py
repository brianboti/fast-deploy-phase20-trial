import platform

import django
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, "trial/index.html", {"django": django.get_version(), "python": platform.python_version(),
                                                "users": User.objects.count()})


def health(request):
    return JsonResponse({"ok": True})
