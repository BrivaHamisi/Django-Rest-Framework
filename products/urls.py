from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list),
    path('products/', views.ProductCreateAPIView.as_view()),
    path('products/<int:pk>/', views.ProductDetailAPIView.as_view()),
]