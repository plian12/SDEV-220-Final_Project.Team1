from django.urls import path
from . import views

# This code is defining URL patterns for a Django application. Each `path` function call
# specifies a URL pattern along with the corresponding view function that should be called when that
# URL is accessed.
urlpatterns = [
    path('', views.home, name='home'),
    path('customer_lookup/', views.customer_lookup, name='customer_lookup'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
]