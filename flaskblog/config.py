import os
from dotenv import load_dotenv;

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SEC_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('PORT')
    MAIL_USE_TLS = os.environ.get('TLS')
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')