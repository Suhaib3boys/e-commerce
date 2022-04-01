from django.urls import path
from . import views

app_name = 'shope'
urlpatterns = [
    path('', views.AllProdCat, name='AllProdCat'),
    path('<slug:c_slug>/', views.AllProdCat, name='product_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProductDetail, name='ProductDetail'),

]
