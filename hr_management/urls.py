from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('core.urls')),
    path('companys/', include('companys.urls')),
    path('collaborators/', include('collaborators.urls')),
    path('departments/', include('departments.urls')),
    path('documents/', include('documents.urls')),
    path('overtime-record/', include('overtime_worked.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
