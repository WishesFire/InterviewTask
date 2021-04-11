from flask import render_template, make_response, Blueprint

error_hd = Blueprint('errors', __name__)


@error_hd.app_errorhandler(404)
def page_not_found(error):
    return make_response(render_template('page404.html'), 404)


@error_hd.app_errorhandler(408)
def page_timeout(error):
    return make_response(render_template('page404.html'), 408)


@error_hd.app_errorhandler(400)
def page_bad_request(error):
    return make_response(render_template('page404.html'), 400)
