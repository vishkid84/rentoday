from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('<int:listing_id>/', views.listing_detail, name='listing_detail'),
    path('add/', views.add_listing, name='add_listing'),
]
