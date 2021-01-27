from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from accounts import views as user_views


urlpatterns = [
    path('youcantaccess/', admin.site.urls),
    path('', include('accounts.urls')),
    path('notifications/', include('notis.urls')),
    path('questions/', include('qapp.urls')),
    path('blog/', include('blog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
