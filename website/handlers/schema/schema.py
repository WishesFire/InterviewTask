from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from website.handlers.services import ValidatorSchema, SaveSchema
from website.database.models_schema import Schema
from flask_login import login_required, current_user
from . import task_schema

schema_views = Blueprint('schema', __name__)


@schema_views.route('/profile/create_schema', methods=["POST", "GET"])
@login_required
def new_schema():
    if request.method == 'POST':
        schema_name = request.form.get('schema_name')
        schema_separator = request.form.get('schema_select')
        schema_character = request.form.get('schema_character')
        column_count = request.form.get('column_count')
        column_list = []

        for _ in column_count:
            elem_list = [request.form.get('column_name'),
                         request.form.get('column_type'),
                         request.form.get('column_order')]
            column_list.append(elem_list)

        valid = ValidatorSchema(schema_name, column_list)
        schema_name = valid.name_valid()
        if not valid.exist_duplicate(schema_name):
            flash('Такое название уже есть!)')
            return redirect(url_for('base.new_schema'))

        SaveSchema(schema_name, schema_separator, schema_character, column_list, current_user.id)
        return redirect(url_for('base.profile'))

    content = {'user': current_user, 'name': current_user.username}
    return render_template('data_form.html', **content)


@schema_views.route('/schema/<slug>', methods=["POST", "GET"])
@login_required
def schema_detail(slug):
    if request.method == 'GET':
        status = Schema.query.filter_by(user=current_user.id, slug=slug).first()
        if not status:
            abort(404)

    if request.method == 'POST':
        rows_number = int(request.form.get('rows'))
        task_schema.generate_fake_data.delay(rows_number)

    #TODO получити силки на файли з такою Schema
    content = {'user': current_user, 'name': current_user.username, 'path': slug}
    return render_template('schema_detail.html', **content)
