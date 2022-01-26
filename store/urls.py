from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:id>/', views.ProductDetail.as_view()),
    path('collections/', views.collections_list),
    path('collections/<int:pk>/', views.collections_detail, name='collection-detail'),
]
