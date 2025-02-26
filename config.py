import os
from dotenv import load_dotenv

# 🔹 Carrega as variáveis do arquivo .env
load_dotenv()

class Config:
    """Configurações gerais"""
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = os.getenv("FLASK_ENV", "development") == "development"
    HOST = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
    PORT = int(os.getenv("FLASK_RUN_PORT", 5000))

class DevelopmentConfig(Config):
    """Configurações para desenvolvimento"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurações para produção"""
    DEBUG = False
