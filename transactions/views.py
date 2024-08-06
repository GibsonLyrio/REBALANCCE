from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect 
from .models import Transactions
from django.http import HttpResponse, HttpResponseRedirect, QueryDict

# Create your views here.
def index(request):
  result = Transactions.objects.all()
  return render(request, 'index.html', { 'transactions': result })

@csrf_protect
def form(request):
  if request.method == 'GET':
    return render(request, 'form.html')

  if request.method == 'POST':
    newTransactions = Transactions()
    
    if request.POST.get('type') == 'receita':
      newTransactions.type = True
    if request.POST.get('type') == 'despesa':
      newTransactions.type = False

    newTransactions.value = request.POST.get('value')
    newTransactions.description = request.POST.get('description')
    newTransactions.save()
    
    return HttpResponseRedirect('/transactions')
  
  if request.method == 'PUT':
    print('PUT method')
    print(request.PUT.get('type'))
    return HttpResponse.status_code(200)
