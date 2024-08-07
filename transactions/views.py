from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect 
from .models import Transactions
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.urls import reverse

### Create your views here.
# index page handler:
def index(request):
  if request.method != 'GET':
    # early return, method no allowed
    return HttpResponse(status_code=405)
  
  context = {}
  context['transactions'] = Transactions.objects.all()

  # get all in database, and if isn't have any, redirect do first form:
  if context['transactions'].count() == 0:
    return render(request, 'first.html', context)

  # otherwise, return de index page with all transactions: 
  return render(request, 'index.html', context)
# ----

# first form page handler:
def first(request):
  context = {}
  return render(request, 'first.html', context)
# ----

# transaction form page handler:
def form(request):
  context = {}
  return render(request, 'form.html', context)
# ----

# add transaction backend handler:
def formAdd(request):
  context = {}
  context['transaction'] = request.POST

  transaction = Transactions()
  transaction.type = context['transaction'].get('type')
  transaction.value = context['transaction'].get('value')
  transaction.description = context['transaction'].get('description')
  transaction.save()
  
  return HttpResponseRedirect(reverse('index'))
# ----

#  edit transaction backend handler:
def formEdit(request):
  context = {}
  context['transaction'] = request.POST

  if 'update' in request.POST:
    id = request.POST.get('update')
    transaction = Transactions.objects.get(id=id)
    context['transaction'] = transaction
    context['editMode'] = True
    return render(request, 'form.html', context)

  if 'delete' in request.POST:
    id = request.POST.get('delete')
    transaction = Transactions.objects.get(id=id)
    transaction.delete()

  return HttpResponseRedirect(reverse('index'))
# ---

# update transaction data backend function:
def updateTransaction(request):
  context = {}
  context['transaction'] = request.POST

  transaction = Transactions.objects.get(id=context['transaction'].get('id'))
  transaction.type = context['transaction'].get('type')
  transaction.value = context['transaction'].get('value')
  transaction.description = context['transaction'].get('description')
  transaction.save()

  return HttpResponseRedirect(reverse('index'))
# ----
