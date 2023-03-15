from django.shortcuts import render


def home(request):
    return render(request, 'Home.html')


def reverse(request):
    return render(request, 'reverse.html')