import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-default-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///spendwise.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
