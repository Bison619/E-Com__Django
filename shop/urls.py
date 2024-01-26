from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="homeShop"),
    path("aboutus/", views.aboutus, name="Aboutus"),
    path("contactus/", views.contactus, name="Contactus"),
    path("productview/", views.productview, name="Productview"),
    path("tracking/", views.tracking, name="Tracking"),
    path("checkout/", views.checkout, name="Checkout"),
    path("search/", views.search, name="Search")
    
]