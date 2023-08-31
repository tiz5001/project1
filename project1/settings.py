from .settings_common import *

from dotenv import load_dotenv

import os
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
#SECRET_KEY ='django-insecure-cl6$%!8&8c)qp#2(&1#f)(#a#o)rwogpm+dp5mx=ikuvwfiun!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.environ.get('DOMAIN')]



