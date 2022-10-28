from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('listings/', views.listings_index, name='index'),
    path('my_listings/', views.listings_index, name='my_listings'),
    path('listings/<int:listing_id>/', views.listings_detail, name='detail'),
    path('listings/create/', views.ListingCreate.as_view(), name='listings_create'),
    path('listings/<int:pk>/update/', views.ListingUpdate.as_view(), name='listings_update'),
    path('listings/<int:pk>/delete/', views.ListingDelete.as_view(), name='listings_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('listings/<int:listing_id>/add_comment/<int:commenter_id>', views.add_comment, name='add_comment'),
    path('listings/<int:listing_id>/add_comment/', views.add_comment, name='add_comment'),
]
