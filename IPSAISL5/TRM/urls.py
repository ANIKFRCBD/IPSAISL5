from django.urls import path
from . import views as TRM

urlpatterns = [

    path('dataproceecing',TRM.trmpage,name="processing"),
]
