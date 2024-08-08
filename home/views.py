from django.shortcuts import render, HttpResponse

def home(request):
  context = {}
  return render(request, 'home.html', context)
