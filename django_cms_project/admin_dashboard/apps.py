from django.apps import AppConfig

class AdminDashboardConfig( AppConfig ):
    name = 'admin_dashboard'

    def ready( self ):
        from admin_dashboard import signals 
