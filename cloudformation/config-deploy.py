#     Copyright 2014 Netflix, Inc.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
# Insert any config items here.
# This will be fed into Flask/SQLAlchemy inside security_monkey/__init__.py

LOG_LEVEL = "DEBUG"
LOG_FILE = "/sm/logs/security_monkey-deploy.log"

SQLALCHEMY_DATABASE_URI = 'postgresql://{DBUSER}:{DBPASSWORD}@{DBHOST}:5432/{DBNAME}'

SQLALCHEMY_POOL_SIZE = 50
SQLALCHEMY_MAX_OVERFLOW = 15
ENVIRONMENT = 'ec2'
USE_ROUTE53 = False
FQDN = '{FQDN}'
API_PORT = '5000'
WEB_PORT = '443'
FRONTED_BY_NGINX = True
NGINX_PORT = '443'
WEB_PATH = '/static/ui.html'

SECRET_KEY = '{SECRET}'

DEFAULT_MAIL_SENDER = 'securitymonkey@example.com'
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = False
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = '{SALT}'
SECURITY_POST_LOGIN_VIEW = 'https://{FQDN}/'

# This address gets all change notifications
SECURITY_TEAM_EMAIL = ['securityteam@example.com']
