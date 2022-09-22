from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('core.urls')),
    path('companys/', include('companys.urls')),
    path('collaborators/', include('collaborators.urls')),
    path('departments/', include('departments.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
