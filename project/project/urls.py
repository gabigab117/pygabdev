from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('search.urls')),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('sitemap.xml', sitemap),
    path('', include(wagtail_urls)),

]

if settings.ENV != "PROD":
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
