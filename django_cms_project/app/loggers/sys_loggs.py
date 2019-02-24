import logging
import time

def setup_logger_info( name, log_file = 'app/logs/app_info.reg', level = logging.INFO ):
    formatter = logging.Formatter('%(name)-10s%(asctime)s %(levelname)s %(message)s')
      
    handler = logging.FileHandler( log_file )        
    handler.setFormatter( formatter )

    logger = logging.getLogger( name )
    logger.setLevel( level )
    logger.addHandler( handler )

    return logger
    

def setup_logger_warning( name, log_file = 'app/logs/app_warning.reg', level = logging.WARNING ):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler( log_file )        
    handler.setFormatter( formatter )

    logger = logging.getLogger( name )
    logger.setLevel( level )
    logger.addHandler( handler )

    return logger

def setup_logger_debug( name, log_file = 'app/logs/app_debug.reg', level = logging.DEBUG ):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler( log_file )        
    handler.setFormatter( formatter )

    logger = logging.getLogger( name )
    logger.setLevel( level )
    logger.addHandler( handler )

    return logger

def setup_logger_critical( name, log_file = 'app/logs/app_critical.reg', level = logging.CRITICAL ):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler( log_file )        
    handler.setFormatter( formatter )

    logger = logging.getLogger( name )
    logger.setLevel( level )
    logger.addHandler( handler )

    return logger

def setup_logger_error( name, log_file = 'app/logs/app_errors.reg', level = logging.ERROR ):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler( log_file )        
    handler.setFormatter( formatter )

    logger = logging.getLogger( name )
    logger.setLevel( level )
    logger.addHandler( handler )

    return logger


# função auxiliar 