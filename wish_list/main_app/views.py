from django.shortcuts import render,redirect
from .models import Wishlist
from .forms import WishlistForm
 # Create your views here.
def index(request):
    wishlist = Wishlist.objects.all()
    wishlist_form = WishlistForm()
    return render (request, 'index.html', {'wishlist': wishlist, 'wishlist_form': wishlist_form})


def add_wish(request):
    form = WishlistForm(request.POST)
    if form.is_valid:
        form.save()
    return redirect('index')

