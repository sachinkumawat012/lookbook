from django.urls import path
from post import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path("post", views.post, name="post"),
    path("main/", views.main, name="main"),
    path("details/<id>", views.details, name="details"),
    path("like", views.like, name="like"),
    path("follow/<id>", views.follow, name="follow"),
    path("profile/<id>", views.profile, name="profile"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
