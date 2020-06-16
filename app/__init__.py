import logging
from logging.handlers import RotatingFileHandler
import os

from flask import Flask,current_app
from config import Config


def init_app(config_class=Config):
    """工厂函数"""

    app = Flask(__name__)
    app.config.from_object(Config)

  
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)


    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # 添加新属性

    if not app.debug:

        # 记录日志
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/blog.log', maxBytes=10240,
                                        backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('程序启动')

    return app
    