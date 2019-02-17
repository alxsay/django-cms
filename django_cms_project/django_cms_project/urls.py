from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls import include, url

from admin_dashboard.urls import urlpatterns
from app.urls import urlpatterns
from chat.urls import urlpatterns
from cms.urls import urlpatterns

admin.autodiscover()

urlpatterns = [
    path( 'admin/', admin.site.urls ),
    path( '', include( 'admin_dashboard.urls' ) ),
    path( '', include( 'app.urls' ) ),
    path( '', include( 'chat.urls' ) ),
    path( '', include( 'cms.urls' ) ),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include( debug_toolbar.urls )),
    ] + urlpatterns
