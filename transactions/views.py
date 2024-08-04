from django.shortcuts import render
from .models import Transactions

# Create your views here.
def index(request):
  result = Transactions.objects.all()
  return render(request, 'index.html', { 'transactions': result })

def form(request):
  return render(request, 'form.html')
