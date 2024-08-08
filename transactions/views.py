from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Transactions
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.urls import reverse

# index page handler
def index(request):
  context = {}

  # early return, method no allowed
  if request.method != 'GET':
    return HttpResponse(status_code=405)

  # tries get transactions of database
  try:
    context['transactions'] = Transactions.objects.all()
    print(f'\033[34mTransações encontradas = [\n {context['transactions']}\n]\033[m')
    context['getAllTransactionsSuccess'] = True
  except:
    # if get operation failed
    context['getAllTransactionsSuccess'] = False
    return HttpResponse('<H1>Não foi possível encontrar as transações</H1>')

  # if isn't have any, set first transaction flag
  if context['transactions'].count() == 0:
    context['firstTransaction'] = True
    return render(request, 'first.html', context)
  context['firstTransaction'] = False

  # return de index page with all transactions
  return render(request, 'index.html', context)
# ----

# first form page handler
# TODO: remove this method and add in the index page the handler of this function of 'first transaction' warning
@csrf_protect
def first(request):
  context = {}

  # early return, method no allowed
  if request.method != 'GET':
    return HttpResponse(status_code=405)

  return render(request, 'first.html', context)
# ----

# transaction form page handler:
@csrf_protect
def form(request):
  context = {}

  # early return, method no allowed
  if request.method != 'GET':
    return HttpResponse(status_code=405)

  return render(request, 'form.html', context)
# ----

# add transaction backend handler
@csrf_protect
def formAdd(request):
  context = {}

  # early return, method no allowed
  if request.method != 'POST':
    return HttpResponse(status_code=405)

  context['transaction'] = request.POST   # get request info

  # tries create a new transaction and save in DB
  try:
    transaction = Transactions()  # new instance of Transactions
    # setting the values fields of new transaction
    transaction.type = context['transaction'].get('type')
    transaction.value = context['transaction'].get('value')
    transaction.description = context['transaction'].get('description')
    # save this new transaction with infos
    transaction.save()
    context['addTransactionSuccess'] = True
  except:
    context['addTransactionSuccess'] = False
    return HttpResponse('<H1>Não foi possível salvar transação</H1>')

  return HttpResponseRedirect(reverse('index'))
# ----

#  edit transaction backend handler
@csrf_protect
def formEdit(request):
  context = {}

  # early returnn method not allowed
  if request.method != 'POST':
    return HttpResponse(status=405) 

  context['transaction'] = request.POST   # get request info

  # verify which operation need be do
  if 'update' in request.POST:
    id = request.POST.get('update')
    # tries get transaction by id to be updated
    try:
      transaction = Transactions.objects.get(id=id)
      context['getTransactionSuccess'] = True
    except:
      context['getTransactionSuccess'] = False
      return HttpResponse('<H1>Não foi possível encontrar a transação selecionada</H1>')
    context['transaction'] = transaction
    context['editMode'] = True
    return render(request, 'form.html', context)

  if 'delete' in request.POST:
    id = request.POST.get('delete')
    try:
      transaction = Transactions.objects.get(id=id)
      transaction.delete()
      context['getTransactionSuccess'] = True
    except:
      context['getTransactionSuccess'] = False
      return HttpResponse('<H1>Não foi possível encontrar a transação selecionada</H1>')

  return HttpResponseRedirect(reverse('index'))
# ---

# update transaction data backend function
@csrf_protect
def updateTransaction(request):
  context = {}

  # early return, method no allowed
  if request.method != 'POST':
    return HttpResponse(status_code=405)
  
  context['transaction'] = request.POST   # get request info

  # tries update the transaction in DB
  try:
    transaction = Transactions.objects.get(id=context['transaction'].get('id'))
    transaction.type = context['transaction'].get('type')
    transaction.value = context['transaction'].get('value')
    transaction.description = context['transaction'].get('description')
    transaction.save()
    context['updateTransactionSuccess'] = True
  except:
    context['updateTransactionSuccess'] = False
    return HttpResponse('Não foi possível atualizar a transação')  

  return HttpResponseRedirect(reverse('index'))
# ----
