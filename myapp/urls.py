from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("", views.home, name="homepage"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("index/", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("logouts/", views.logouts, name="logouts"),
    path("main/", views.main, name="main"),
    path("details/<id>", views.details, name="details"),


    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
