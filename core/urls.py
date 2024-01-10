"""
URL configuration for core project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from post.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('2/', index2, name='index2'),
    path('3/', index3, name='index3'),
    path('4/', index4, name='index4'),
    path('5/', index5, name='index5'),
    path('about/', adout, name='about'),
    path('menu/', menu, name='menu'),
    path('shop/', shop, name='shop'),
    path('shop_details/', shop_details, name='shop_details'),
    path('cart/', cart, name='cart'),
    path('wishlist/', wishlist, name='wishlist'),
    path('reservation/', reservation, name='reservation'),
    path('faq/', faq, name='faq'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('pnf/', pnf, name='pnf'),
    path('coming_soon/', coming_soon, name='coming_soon'),
    path('terms_conditions/', terms_conditions, name='terms_conditions'),
    path('blogs/', blogs, name='blogs'),
    path('blog_details/', blog_details, name='blog_details'),
    path('contact/', contact, name='contact'),
    path('checkout/', checkout, name='checkout'),
]