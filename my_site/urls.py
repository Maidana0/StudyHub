from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

handler404 = "pages.views.handler404"
from django.urls import re_path

# from django.conf import settings
from django.views.static import serve

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
