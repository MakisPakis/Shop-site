from django.urls import path
from .views import cart_view, cart_add_view, cart_delete_view, cart_update_view

app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='cart_view'),
    path('add/', cart_add_view, name='add_to_cart'),
    path('delete/', cart_delete_view, name='delete_to_cart'),
    path('update/', cart_update_view, name='update_to_cart'),
]
