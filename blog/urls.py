from django.urls import path
from blog import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    path('', views.test, name='test'),
    path('<int:blog_id>/', views.detail, name='detail'),

]
# we have to import static, this functinality from Django project which we have import here.

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# search django media tutorial can help finding on web

