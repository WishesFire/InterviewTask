from flask import Blueprint, render_template, request, jsonify
from website.database.models_schema import Schema, ColumnSchema
from psycopg2 import Error
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
                exact_table = Schema.query.filter_by(user=current_user.id, name=data['name']).first_or_404()
                table_id = exact_table.id
                ColumnSchema.query.filter_by(schema_id=table_id).delete()
                db.session.delete(exact_table)
                db.session.commit()
            except Error:
                db.session.rollback()

            return jsonify({"status": "delete"})

    tables = Schema.query.filter_by(user=current_user.id)
    content = {'user': current_user, 'name': current_user.username, 'tables': tables}
    return render_template('user/profile.html', **content)


