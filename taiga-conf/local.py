# Please modify this file as needed, see the local.py.example for details:
# https://github.com/taigaio/taiga-back/blob/master/settings/local.py.example
#
# Importing docker provides common settings, see:
# https://github.com/benhutchins/docker-taiga/blob/master/docker-settings.py
# https://github.com/taigaio/taiga-back/blob/master/settings/common.py
from .docker import *

PUBLIC_REGISTER_ENABLED = False
DEBUG = False
TEMPLATE_DEBUG = False

## Slack
# https://github.com/taigaio/taiga-contrib-slack
INSTALLED_APPS += ["taiga_contrib_slack"]

## LDAP
# see https://github.com/ensky/taiga-contrib-ldap-auth
# INSTALLED_APPS += ["taiga_contrib_ldap_auth"]

# EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'email-smtp.us-west-2.amazonaws.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'AKIAICN6QFIQC5KVOVYA'
EMAIL_HOST_PASSWORD = 'AtOqwrp5ichBpqoKsW2vF3JS4ha8gDrUD1bjY0dxXgld'
DEFAULT_FROM_EMAIL = 'sending@loansolutions.ph'
