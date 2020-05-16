from django.urls import path
from blog import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
]
# we have to import static, this functinality from Django project which we have import here.

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# search django media tutorial can help finding on web

