from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    path('products/delete/<int:id>/', views.product_delete),
    path('collections/', views.collection_list),
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail'),
    path('collections/delete/<int:pk>/', views.collection_delete),
    path('test', views.test)
]
