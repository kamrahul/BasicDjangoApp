from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<h1>Hello world</h1>')


def about_page(request):
    return HttpResponse('<h1>About page</h1>')


def contact_page(request):
    return HttpResponse('<h1> Contact page</h1>')