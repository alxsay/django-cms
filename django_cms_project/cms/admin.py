#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
arquivo: [ implantacao.admin.py ]
autor: Saymon de Oliveira Souza ( saymon.souza@cogni.group )
propósito: registro de apps no painel admin para cruds rápidos
data criação: 07/12/2018
última atualização: 10/11/2018

"""

from django.contrib import admin
from .models import *

admin.site.register( CmsUser )
admin.site.register( CmsUserMeta )
admin.site.register( CmsPost )
admin.site.register( CmsPostMeta )
admin.site.register( CmsComment )
admin.site.register( CmsCommentMeta )
admin.site.register( CmsTerm )
admin.site.register( CmsTermMeta )
admin.site.register( CmsTaxonomy )
admin.site.register( CmsLink )
admin.site.register( CmsOption )
