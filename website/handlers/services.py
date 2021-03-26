from website import db
from website.database.models_schema import Schema, ColumnSchema


class ValidatorSchema:
    def __init__(self, schema_name, column_list):
        self.name = schema_name
        self.list = column_list

    def name_valid(self):
        if isinstance(self.name, str):
            return self.name.title()
        else:
            return str(self.name)

    @staticmethod
    def exist_duplicate(name):
        status = Schema.query.filter_by(name).first()
        if status is None:
            return True
        return False


class SaveSchema:
    def __init__(self, schema_name, separator, character, column_list, user):
        self._schema_name = schema_name
        self._separator = separator
        self._character = character
        self._column_list = column_list
        self._user = user

        self.__save_schema()
        self.__save_column()

    def __save_schema(self):
        count = Schema.query.filter_by(user=self._user).count()
        self.new_schema = Schema(name=self._schema_name, separate=self._separator,
                                 character=self._character, user=self._user, order=count+1)
        db.session.add(self.new_schema)
        db.session.commit()

    def __save_column(self):
        for block_column in self._column_list:
            new_column = ColumnSchema(name=block_column[0], type=block_column[1], schema=self.new_schema.id)
            db.session.add(new_column)
            db.session.comit()
