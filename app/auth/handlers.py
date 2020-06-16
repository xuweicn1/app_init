from app.auth import bp

@bp.route('/login')
def index():
    return '这是登陆页面'
