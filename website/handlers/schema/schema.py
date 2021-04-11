from flask import Blueprint, render_template, request, redirect, url_for, flash, abort, jsonify
from website.tools.status_choice import FULL_LIST_CHOICE
from website.handlers.utils import ValidatorSchema, SaveSchema
from website.database.models_schema import Schema, FileSchema
from flask_login import login_required, current_user
from celery.result import AsyncResult
from . import task_schema

schema_views = Blueprint('schema', __name__)


@schema_views.route('/profile/create_schema', methods=["POST", "GET"])
@login_required
def new_schema():
    if request.method == 'POST':
        schema_name = request.form.get('schema_name')
        schema_separator = request.form.get('schema_select')
        column_names_list = request.form.getlist('column_name')
        column_types_list = request.form.getlist('column_type')
        column_orders_list = request.form.getlist('column_order')
        column_list = []

        column_types_list = ValidatorSchema.remark_choice(column_types_list)

        for elem in zip(column_names_list, column_types_list, column_orders_list):
            column_list.append(list(elem))

        schema_name = ValidatorSchema.name_valid(schema_name)
        if not ValidatorSchema.exist_duplicate(schema_name, current_user.id):
            flash('Такое название уже есть!)')
            return redirect(url_for('schema.new_schema'))

        SaveSchema(schema_name, schema_separator, column_list, current_user.id)
        return redirect(url_for('base.profile'))

    content = {'user': current_user, 'name': current_user.username, 'types': FULL_LIST_CHOICE}
    return render_template('data_form.html', **content)


@schema_views.route('/schema/<slug>', methods=["POST", "GET"])
@login_required
def schema_detail(slug):
    if request.method == 'GET':
        status = Schema.query.filter_by(user=current_user.id, slug=slug).first()
        if not status:
            abort(404)

        downloads_file = FileSchema.query.filter_by(schema=status.id, user=current_user.id)
        content = {'user': current_user, 'name': current_user.username,
                   'slug': slug, 'files': downloads_file.order_by(FileSchema.created_at)}
        return render_template('schema_detail.html', **content)

    if request.method == 'POST':
        content = request.json
        if content['status_client_task'] == 'sending':
            rows_number = content['count']
            user = current_user.id
            schema = Schema.query.filter_by(user=user, slug=slug).first()
            separator = schema.separate
            task = task_schema.generate_fake_data.delay(rows_number, separator, user, schema.id)
            return jsonify({"task_id": task.id, "task_status": "processing"})

        elif content['status_client_task'] == 'waiting':
            task_id = content['task_id']
            task_result = AsyncResult(task_id).result
            if task_result:
                result = {
                    "task_id": task_id,
                    "task_status": "ready",
                }
            else:
                result = {
                    "task_id": task_id,
                    "task_status": "processing",
                }
            return jsonify(result)

