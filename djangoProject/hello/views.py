from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")  # render() function combines a template with a context dictionary to
    # return an HttpResponse object with that rendered text.


def Shruti(request):
    return HttpResponse("Hello, This is Shruti.")


def Stark(request):
    return HttpResponse("Hello, This is Tony Stark.")


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
        # capitalize() method returns a copy of the string with only its first character to be a capital letter.
    })  # key: name, value: name.capitalize()
