from django.urls import path
from .views import *
from .views import admin_login
urlpatterns = [
    path('user/',index,name='index'),
    path('admin_page/',admin_page,name='admin_page'),
    path('product_add/',add_product.as_view(),name='add_product'),
    path('product_update/<int:pk>',update_product.as_view(),name='update_product'),
    path('product_delete/<int:pk>',delete_product,name='delete_product'),
    path('', admin_login, name='admin_login'),

]
