"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

handler404 = "pages.views.handler404"
from django.urls import re_path

# from django.conf import settings
from django.views.static import serve

# handler404 = "home.views.handler404"
# DENTRO DE URLPATHENS:
#
url_files = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("apuntes/", include("study_hub.urls")),
    path("cuenta/", include("account.urls")),
    path("tinymce/", include("tinymce.urls")),
]

if settings.DEBUG == False:
    urlpatterns += url_files
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
