from app.api import bp

@bp.route('/token')
def index():
    return '这是api 取token页面'
