import os, sys
sys.path.append('/var/www/gitpaste')
sys.path.append('/var/www/gitpaste/saic')
os.environ['DJANGO_SETTINGS_MODULE'] = 'saic.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
