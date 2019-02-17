from django.forms.models import model_to_dict
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from app.models import *

import json

@receiver( post_save, sender = None )
def test_signals( sender, instance, created, **kwargs ):
    #if created:
    print( "Signal funcionando" )
    token_secret = '6OIPRG'
    channel_layer = get_channel_layer()
    async_to_sync(  channel_layer.group_send )( 
            'group_%s' % token_secret, 
            { 
                'type' :  'send_message',     
                'data' : 'empresa qualquer alterado na trigger' 
            }  
     )

def send_message( self, event ):
    message_to_be_sended = event[ 'data' ]
    channel_layer = get_channel_layer()
    async_to_sync( channel_layer.send )( text_data = json.dumps({
        'message' : message_to_be_sended
    }))
    
