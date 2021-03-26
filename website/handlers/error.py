from flask import render_template, make_response, Blueprint

error_hd = Blueprint('errors', __name__)


@error_hd.app_errorhandler(404)
def page_not_found(error):
    return make_response(render_template('page404.html'), 404)
