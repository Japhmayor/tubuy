from django.shortcuts import render


def docs(request):
    return render(request, 'index.html')
