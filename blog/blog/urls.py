
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import never_cache
from django.views.generic import RedirectView
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls')),
    path('accounts/', include('blogs.urls')),
    path('', RedirectView.as_view(url='blogs/', permanent=True))
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)