from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/media/', include('media.urls')),
    path('api/geocoding/', include('geocoding.urls')),
]
