from django.urls import path

from .views import home, searchNavbar


urlpatterns = [
    path("", home, name="home"),
    # POST require
    path("search/publications/", searchNavbar, name="search"),
    # GET require
]
