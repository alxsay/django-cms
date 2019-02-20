from django.forms.models import model_to_dict
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from cms.models import CmsPost, CmsUser

import json

@receiver( post_save, sender = CmsPost )
def notify_post_created( sender, instance, created, **kwargs ):
    if created:
        print( "Post salvo com sucesso." )
    else:
        print( "Post alterado com sucesso." )


@receiver( post_save, sender = CmsUser )
def notify_user_saved( sender, instance, created, **kwargs ):
    
    if created:
        print( "Usuário salvo com sucesso." )
    else:
        print( "Usuário alterado com sucesso." )
