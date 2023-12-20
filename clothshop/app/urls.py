from django.urls import path
from app import views

urlpatterns=[
    path('',views.home),
    path('addnew',views.addnew),
    path('edit/<tid>',views.edit),
    path('delete/<tid>',views.delete)

]