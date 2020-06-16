from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    # return render_template('errors/404.html'), 404
    return '没有此页:404错误', 404


@bp.app_errorhandler(500)
def internal_error(error):
    # return render_template('errors/500.html'), 500
    return '系统错误:500错误', 500