from django.urls import path
from post import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path("post", views.post, name="post"),
    path("main/", views.main, name="main"),
    path("details/<id>", views.details, name="details"),
    path("like/", views.like, name="like"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
