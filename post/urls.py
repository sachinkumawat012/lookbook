from django.urls import path
from post import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path("post", views.post, name="post"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
