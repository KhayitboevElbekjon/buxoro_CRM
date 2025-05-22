import os
from whitenoise import WhiteNoise
from pathlib import Path
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Study_center.settings')
BASE_DIR = Path(__file__).resolve().parent.parent

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
