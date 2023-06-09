import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = get_wsgi_application()
application = get_wsgi_application()

WSGI_APPLICATION = 'vercel_app.wsgi.app'
# app = application
