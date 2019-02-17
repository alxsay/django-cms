from django.conf.urls import url
from django.urls import path

from channels.routing import ProtocolTypeRouter

from chat.consumers import ChatConsumer


websocket_urlpatterns = [
    path( "chat/stream/<str:group_name>/", ChatConsumer ),
]

