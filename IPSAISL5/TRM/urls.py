from django.urls import path
from . import views as TRM

urlpatterns = [

    path('dataproceecing',TRM.trmpage,name="processing"),
    path('approval', TRM.trm_list_approver,name='trmapproval'),
]
