from django.urls import path
from ProductInventory import views


urlpatterns = [

    path('products/', views.ProductView.as_view(), name='products')
    
]
