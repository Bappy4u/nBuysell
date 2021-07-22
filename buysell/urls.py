
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homeview'),
    path('login/', views.loginview, name='loginview'),
    path('signup/', views.signup_view, name='signupview'),
    path('add-post/', views.addpostview, name='addpostview'),
    path('logout/', views.logoutview, name='logoutview'),
    path('all-ads/<location>/', views.sorted_locview, name='sorted_locview'),
    path('category/<category>/', views.categoryview, name='categoryview'),
    path('product/<url>/', views.productview, name='productview'),
    path('search/query=<query>', views.searchview, name='searchview'),
    path('upload/<id>', views.uploadview, name='uploadview'),
    path('uploads/', views.uploadview2, name='uploadview2'),
    path('edit/<pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('delete/<pk>/', views.ProductDelete.as_view(), name='product_delete'),
    path('save/<id>/', views.productSaveview, name='product_saveview'),
    path('unlike/<id>/', views.unlineview, name='product_unlikeview'),
    path('saved/<user>/', views.savedproductview,
         name='product_savedproductview'),
    path('my-products/<user>/', views.myproductview, name='myproductview'),
]
