from django.urls import path
from .views import home, about, contacts, product_list, product_detail, product_search

urlpatterns = [
    path('search/', product_search, name='product_search'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
    path('product_list/', product_list, name='product_list'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('', home, name='home'),
]