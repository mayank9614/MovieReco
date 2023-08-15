import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'afde5bb5a16049d885aa13e93f5187de'
