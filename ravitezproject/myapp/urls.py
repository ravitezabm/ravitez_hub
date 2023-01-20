
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.loginfun,name='login'),
    path('shop/',views.shopfun,name='shop'),
    path('login/',views.createaccountfun,name='createaccount')
    
]
