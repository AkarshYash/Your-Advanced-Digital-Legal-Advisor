import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'legalease_ai_advanced_secret_key_2024'
   
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///legalease_advanced.db'
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx'}
    
    # Email configuration (for future use)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # Pagination
    POSTS_PER_PAGE = 10
    
    # Languages supported
    SUPPORTED_LANGUAGES = {
        'en': 'English',
        'hi': 'हिंदी',
        'ta': 'தமிழ்',
        'te': 'తెలుగు',
        'bn': 'বাংলা',
        'mr': 'मराठी',
        'gu': 'ગુજરાતી',
        'pa': 'ਪੰਜਾਬੀ',
        'kn': 'ಕನ್ನಡ',
        'ml': 'മലയാളം',
        'or': 'ଓଡ଼ିଆ',
        'as': 'অসমীয়া'
    }
