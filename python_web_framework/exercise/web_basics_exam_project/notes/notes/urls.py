from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.main_content.urls')),
    path('profiles/', include('notes.profiles.urls')),
    path('auth/', include('notes.user_auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
