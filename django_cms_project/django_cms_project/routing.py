from django.urls import path

from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chat.consumers import ChatConsumer
#from chat.routing import websocket_urlpatterns

from django.conf.urls import url, include

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path( "chat/stream/<str:group_name>/", ChatConsumer ),
            #path( '', include( 'chat.routing' ) ),
        ]),
    ),

})
