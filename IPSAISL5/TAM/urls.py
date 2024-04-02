from django.contrib import admin
from django.urls import path,include
from TAM import views as tam

urlpatterns = [
    path('tam/',tam.tampage,name="tam"),
    path('tamapprover/',tam.tam_list_approver,name="tamapprover"),
]