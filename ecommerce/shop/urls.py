from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="about"),
    path("Contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="tracker"),
    path("search/", views.search, name="search"),
    path("productview/", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="checkout")
]