from django.contrib import admin
from django.urls import path
from django.urls import include
from myapp import urls
from post import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('post/', include('post.urls')),
    path('accounts/', include('social_django.urls')),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
