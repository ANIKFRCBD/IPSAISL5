from django.contrib import admin
from django.urls import path,include
from . import views as budget

urlpatterns = [
    path('budget/',budget.budget,name="budget"),
]