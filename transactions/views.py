from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect 
from .models import Transactions
from django.http import HttpResponse, HttpResponseRedirect, QueryDict

# Create your views here.
def index(request):
  context = {}
  context['transactions'] = Transactions.objects.all()
  if Transactions.objects.count() == 0:
    return render(request, 'first.html', context)
  return render(request, 'index.html', context)

@csrf_protect
def form(request):
  context = {}
  if request.method == 'GET':
    return render(request, 'form.html', context)

  if request.method == 'POST':
    print(f'\033[33m some values{request.POST}\033[m')
    if 'delete' in request.POST:
      id = request.POST.get('delete')
      transaction = Transactions.objects.get(id=id)
      transaction.delete()
      return HttpResponseRedirect('/transactions')
    
    if 'edit' in request.POST:
      id = request.POST.get('edit')
      transaction = Transactions.objects.get(id=id)
      context['editMode'] = True
      context['editFormData'] = transaction
      transaction.delete()
      return render(request, 'form.html', context)

    newTransactions = Transactions()

    newTransactions.type = request.POST.get('type')
    newTransactions.value = request.POST.get('value')
    newTransactions.description = request.POST.get('description')

    newTransactions.save()
    
    return HttpResponseRedirect('/transactions')

def first(request):
  return render(request, 'first', context={})
