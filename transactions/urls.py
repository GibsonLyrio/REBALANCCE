from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('first/', views.first, name='first'),
  path('form/', views.form, name='form'),
  path('form/add/', views.formAdd, name='formAdd'),
  path('form/edit/', views.formEdit, name='formEdit'),
  path('update/', views.updateTransaction, name='updateTransaction'),
]
