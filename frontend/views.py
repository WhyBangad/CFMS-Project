from django.http import HttpResponse


def landing(request):
    return HttpResponse("Hello, world. You're at the polls index.")