from flask_restful import Resource, fields
from flask import request
import json
from flask_jwt_extended import jwt_required, get_jwt_identity
from website.database.models_schema import Schema, ColumnSchema
from website import db


class Profile(Resource):
    @jwt_required
    def get(self):
        now_user = get_jwt_identity()
        tables = Schema.query.filter_by(user=now_user.id)
        return tables, 200

    def delete(self):
        now_user = get_jwt_identity()
        data = json.loads(request.data)
        exact_table = Schema.query.filter_by(user=now_user.id, name=data['name']).first_or_404()
        table_id = exact_table.id
        ColumnSchema.query.filter_by(schema_id=table_id).delete()
        db.session.delete(exact_table)
        db.session.commit()
        return "Successfully deleted", 200

