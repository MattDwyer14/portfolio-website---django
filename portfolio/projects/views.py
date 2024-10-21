from django.shortcuts import render

def base(request):
    return render(request, 'projects/base.html')
