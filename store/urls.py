from django.contrib import admin
from django.urls import path
from .views import home, login, signup
from .views import cart

# other  way of importing
from .views.checkout import CheckOut
from .views.orders import OrderView

urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', login.logout, name='logout'),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', OrderView.as_view(), name='orders')

]
