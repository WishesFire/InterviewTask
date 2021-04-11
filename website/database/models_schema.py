from website import db
from website.tools.status_choice import StatusChoices, TypeChoices
from slugify import slugify
from datetime import datetime


class Schema(db.Model):
    __tablename__ = 'schema'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    slug = db.Column(db.String(200))
    separate = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.now())
    user = db.Column(db.ForeignKey('user.id'), nullable=False)
    order = db.Column(db.Integer)
    columns = db.relationship("ColumnSchema")

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'Схема {self.name} создана {self.user}'


class ColumnSchema(db.Model):
    __tablename__ = 'column'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    type = db.Column(db.Enum(TypeChoices))
    schema_id = db.Column(db.Integer, db.ForeignKey('schema.id'), nullable=False)

    def __repr__(self):
        return f'Столбец {self.name}'


class FileSchema(db.Model):
    __tablename__ = 'schema_file'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.Enum(StatusChoices), default=StatusChoices.READY)
    file = db.Column(db.LargeBinary, nullable=True)
    schema = db.Column(db.ForeignKey('schema.id'), nullable=False)
    user = db.Column(db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Файл пользователя {self.user} из схеми {self.schema}'
