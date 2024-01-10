from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    settings = Settings.objects.all()
    return render(request, 'index.html', {'settings': settings})
def index2(request):
    settings = Settings.objects.all()
    return render(request, 'index-2.html', {'settings': settings})
def index3(request):
    settings = Settings.objects.all()
    return render(request, 'index-3.html', {'settings': settings})
def index4(request):
    settings = Settings.objects.all()
    return render(request, 'index-4.html', {'settings': settings})
def index5(request):
    settings = Settings.objects.all()
    return render(request, 'index-5.html', {'settings': settings})
def adout(request):
    settings = About.objects.all()
    return render(request, 'about.html', {'settings': settings})
def menu(request):
    settings = Menu.objects.all()
    return render(request, 'menu.html', {'settings': settings})
def shop(request):
    settings = Shop.objects.all()
    return render(request, 'shop.html', {'settings': settings})
def shop_details(request):
    settings = Shop_Details.objects.all()
    return render(request, 'shop_details.html', {'settings': settings})
def cart(request):
    settings = Cart.objects.all()
    return render(request, 'cart.html', {'settings': settings})
def wishlist(request):
    settings = Wishlist.objects.all()
    return render(request, 'wishlist.html', {'settings': settings})
def checkout(request):
    settings = Checkout.objects.all()
    return render(request, 'checkout.html', {'settings': settings})
def reservation(request):
    settings = Reservation.objects.all()
    return render(request, 'reservation.html', {'settings': settings})
def faq(request):
    settings = FAQ.objects.all()
    return render(request, 'faq.html', {'settings': settings})
def login(request):
    settings = Login.objects.all()
    return render(request, 'login.html', {'settings': settings})
def signup(request):
    settings = Signup.objects.all()
    return render(request, 'signup.html', {'settings': settings})
def pnf(request):
    settings = PNF.objects.all()
    return render(request, '404.html', {'settings': settings})
def coming_soon(request):
    settings = Coming_Soon.objects.all()
    return render(request, 'coming-soon.html', {'settings': settings})
def terms_conditions(request):
    settings = Terms_Conditions.objects.all()
    return render(request, 'terms-conditions.html', {'settings': settings})
def blogs(request):
    settings = Blogs.objects.all()
    return render(request, 'blogs.html', {'settings': settings})
def blog_details(request):
    settings = Blog_Details.objects.all()
    return render(request, 'blog-details.html', {'settings': settings})
def contact(request):
    settings = Contact.objects.all()
    return render(request, 'contact.html', {'settings': settings})


