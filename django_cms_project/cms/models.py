from django.db import models
from django.db.models import signals
from django.forms.models import model_to_dict
from django.db.models.signals import post_save, post_delete
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from asgiref.sync import AsyncToSync
import json


class CmsUser( models.Model ):
    login = models.CharField( max_length = 60 )
    password = models.CharField( max_length = 255 )
    nice_name = models.CharField( max_length = 50 )
    email = models.CharField( max_length = 100 )
    url = models.CharField( max_length = 200 )
    registred = models.DateTimeField()
    activation_key = models.CharField( max_length = 255 )
    status = models.IntegerField( )
    display_name = models.CharField( max_length = 250 )


class CmsUserMeta( models.Model ):
    cms_user = models.ForeignKey( CmsUser, default = None, on_delete = models.CASCADE )
    meta_key = models.CharField( max_length = 255 )
    meta_value = models.TextField()


class CmsPost( models.Model ):
    cms_user = models.ForeignKey( CmsUser, default = None, on_delete = models.CASCADE  )
    date = models.DateTimeField()
    date_gmt = models.DateTimeField()
    content = models.TextField()
    title = models.CharField( max_length = 280 )
    excerpt = models.CharField( max_length = 400 )
    status = models.CharField( max_length = 20 )
    password = models.CharField( max_length = 20 )
    name = models.CharField( max_length = 200 )
    to_ping = models.CharField( max_length = 200 )
    pinged = models.CharField( max_length = 200 )
    modified_date = models.DateTimeField()
    modified_date_gmt = models.DateTimeField()
    content_filtered = models.TextField()
    parent = models.BigIntegerField()
    guid = models.CharField( max_length = 255 )
    menu_order = models.IntegerField( )
    post_type = models.CharField( max_length = 20 )
    post_mime_type = models.CharField( max_length = 100 )
    comment_count = models.BigIntegerField()


class CmsPostMeta( models.Model ):
    cms_post = models.ForeignKey( CmsPost,  default = None, on_delete = models.CASCADE )
    meta_key = models.CharField( max_length = 255 )
    meta_value = models.TextField()


class CmsComment( models.Model ):
    comment_post = models.ForeignKey( CmsPost, on_delete = models.CASCADE )
    cms_user = models.ForeignKey( CmsUser, default = None, on_delete = models.CASCADE )
    author_name = models.CharField( max_length = 60 )
    author_email = models.CharField( max_length = 100 )
    author_url = models.CharField( max_length = 200 )
    author_ip = models.CharField( max_length = 100 )
    date = models.DateTimeField()
    date_gmt = models.DateTimeField()
    content = models.TextField()
    karma = models.IntegerField()
    agent = models.CharField( max_length = 255 )
    comment_type = models.CharField( max_length = 20 )
    approved = models.CharField( max_length = 20 )
    parent = models.BigIntegerField( )



class CmsCommentMeta( models.Model ):
    cms_comment = models.ForeignKey( CmsComment, default = None, on_delete = models.CASCADE )
    meta_key = models.CharField( max_length = 255 )
    meta_value = models.TextField()


# cria os termos das taxonomias
class CmsTerm( models.Model ):
    name = models.CharField( max_length = 200 )
    slug = models.CharField( max_length = 200 )
    term_group = models.BigIntegerField( )


# acrescenta mais propriedades aos termos de uma taxonomia
class CmsTermMeta( models.Model ):
    cms_term = models.ForeignKey( CmsTerm, default = None, on_delete = models.CASCADE )
    meta_key = models.CharField( max_length = 255 )
    meta_value = models.TextField()


# cria as taxonomias
class CmsTaxonomy( models.Model ):
    cms_term = models.ForeignKey( CmsTerm, default = None, on_delete = models.CASCADE )
    posts = models.ManyToManyField( CmsPost )
    name = models.CharField( max_length = 32 )
    description = models.TextField()
    parent = models.BigIntegerField()
    count = models.BigIntegerField()


class CmsLink( models.Model ):
    url = models.CharField( max_length = 255 )
    name = models.CharField( max_length = 255 )
    image = models.CharField( max_length = 255 )
    target = models.CharField( max_length = 255 )
    description = models.CharField( max_length = 255 )
    visible = models.CharField( max_length = 255 )
    owner = models.BigIntegerField()
    rating = models.IntegerField( )
    updated_date = models.DateTimeField()
    rel = models.CharField( max_length = 255 )
    notes = models.TextField()
    rss = models.CharField( max_length = 255 )



class CmsOption( models.Model ):
    name = models.CharField( max_length = 191 )
    value = models.TextField()
    autoload = models.CharField( max_length = 20 )