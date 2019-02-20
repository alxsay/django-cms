from django.apps import AppConfig

class CmsConfig(AppConfig):
    name = 'cms'

    def ready( self ):
        from cms import signals 
