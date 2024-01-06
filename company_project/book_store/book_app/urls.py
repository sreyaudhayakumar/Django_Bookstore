from .import views
from django.urls import path,include

urlpatterns = [
    path('',views.base,name="base"),
    path('base_new',views.base_new,name="base_new"),
    path('account',views.account,name='account'),
    path('login',views.login,name="login"),
    path('add_product',views.add_product,name='add_product'),
    path('product',views.product,name='product'),
    path('product_details',views.product_details,name='product_details'),
    path('edit_product/<int:product_id>/',views.edit_product,name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('update_cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('logout/', views.user_logout, name='logout'),

]
