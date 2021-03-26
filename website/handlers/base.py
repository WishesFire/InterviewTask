from flask import Blueprint, render_template, request, redirect, url_for
from website.database.models_schema import Schema
from flask_login import login_required, current_user
from website import db
import json

base_views = Blueprint('base', __name__)


@base_views.route('/')
def index():
    content = {'user': current_user}
    return render_template('index.html', **content)


@base_views.route('/profile', methods=["POST", "GET"])
@login_required
def profile():
    if request.method == 'POST':
        data = json.loads(request.data)
        if data['status'] == 'delete':
            try:
                Schema.query.filter_by(name=data['name']).delete()
                db.session.commit()
            except:
                db.session.rollback()

            return redirect(url_for('base.profile'))

    tables = Schema.query.filter_by(user=current_user.id)
    content = {'user': current_user, 'name': current_user.username, 'tables': tables}
    return render_template('user/profile.html', **content)


