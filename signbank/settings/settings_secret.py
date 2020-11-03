# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from environs import Env

env = Env()
env.read_env()

# keytest = env("SECRET_KEY")
# print(keytest)
#: Make this unique, and don't share it with anybody. This is used to provide cryptographic signing.
# SECRET_KEY = 'n%me+kd8_9h5hlnty9_&2&47pm(m44ngce8rh#e-5f&6v1i*h_'
SECRET_KEY = env("SECRET_KEY")

#: A list of all the people who get code error notifications. When DEBUG=False and a view raises an exception,
#: Django will email these people with the full exception information.
ADMINS = (
    ('Leslie Joe', env('JOE_EMAIL_ADDRESS')),
    ('Firstname Lastname', "your_email_address@domain.com"),
)

#: The email address that error messages come from, such as those sent to ADMINS and MANAGERS.
#: Note: You can also use the following form 'Webmaster <webmaster@yourdomain.com>'
SERVER_EMAIL='root@localhost'

#: A dictionary containing the settings for all databases to be used with Django.
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': '/path/to/signbank.db',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

#: Is the database engine used postgresql?
DB_IS_PSQL = 'postgresql' in DATABASES['default']['ENGINE']
#: Maximum size of database in bytes, controlled outside of this application. Fill it in if you have a quota.
PSQL_DB_QUOTA = 0
#: The name of a database used.
PSQL_DB_NAME = DATABASES['default']['NAME']

#: The host to use for sending email.
EMAIL_HOST='smtp.localhost'
#: Port to use for the SMTP server defined in EMAIL_HOST.
EMAIL_PORT=1234
#: Default email address to use for various automated correspondence from the site manager(s).
#: Note: You can also use the following form 'Webmaster <webmaster@yourdomain.com>'
DEFAULT_FROM_EMAIL='webmaster@localhost'

# *** Settings for HTTPS ***

#: Whether to use a secure cookie for the session cookie. Cookie is only sent under an HTTPS connection.
#SESSION_COOKIE_SECURE = True

#: Whether to use a secure cookie for the CSRF cookie.
#: - Browsers may ensure that the cookie is only sent with an HTTPS connection.
#CSRF_COOKIE_SECURE = True

#: ** These settings have no effect if SecurityMiddleware is not enabled! **
#: If True, the SecurityMiddleware redirects all non-HTTPS requests to HTTPS (except for those URLs matching
#: a regular expression listed in SECURE_REDIRECT_EXEMPT).
#SECURE_SSL_REDIRECT = True

#: If a URL path matches a regular expression in this list, the request will not be redirected to HTTPS.
#: If SECURE_SSL_REDIRECT is False, this setting has no effect. (Requires SecurityMiddleware).
#: - ELAN as of version 4.9.4 does not support HTTPS correctly,
#: - therefore the externally controlled vocabulary needs to be served with HTTP.
#SECURE_REDIRECT_EXEMPT = [r'dictionary/ecv/', r'dictionary/public-ecv/']

#: All SSL redirects will be directed to this host rather than the originally-requested host.
#: - (Requires SecurityMiddleware  and SECURE_SSL_REDIRECT=True).
#SECURE_SSL_HOST = 'signbank.csc.fi'

#: If True, the SecurityMiddleware sets the X-XSS-Protection: 1; mode=block header on all responses that
#: do not already have it.
#SECURE_BROWSER_XSS_FILTER = True
