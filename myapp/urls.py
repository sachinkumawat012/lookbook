from django.urls import path
from django.urls.conf import include
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
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
