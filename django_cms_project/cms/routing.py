from django.conf.urls import url
from django.urls import path

from channels.routing import ProtocolTypeRouter

from cms.consumers import CmsConsumer


websocket_urlpatterns = [
    path( "cms/stream/<str:group_name>/", CmsConsumer ),
]

