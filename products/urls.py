from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/',home_page,name='homepage'),
    path('',homepage, name='homepage')
    path('menu_s/',MenuAPIView.as_view(),name ='menu_s')
]