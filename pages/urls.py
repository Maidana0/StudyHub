from django.urls import path

from .views import home, searchNavbar, about_me


urlpatterns = [
    path("", home, name="home"),
    path("acerca-de-mi/", about_me, name="about"),
    # POST require
    path("search/publications/", searchNavbar, name="search"),
    # GET require
]
