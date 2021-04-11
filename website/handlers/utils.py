from website import db
from website.database.models_schema import Schema, ColumnSchema
from website.tools.status_choice import TypeChoices


class ValidatorSchema:
    @staticmethod
    def remark_choice(choices):
        lst = []
        for type in choices:
            if type == str(TypeChoices.NAME)[12:]:
                lst.append(TypeChoices.NAME)
            elif type == str(TypeChoices.JOB)[12:]:
                lst.append(TypeChoices.JOB)
            elif type == str(TypeChoices.EMAIL)[12:]:
                lst.append(TypeChoices.EMAIL)
            elif type == str(TypeChoices.DOMAIN)[12:]:
                lst.append(TypeChoices.DOMAIN)
            elif type == str(TypeChoices.PHONE)[12:]:
                lst.append(TypeChoices.PHONE)
            elif type == str(TypeChoices.COMPANY)[12:]:
                lst.append(TypeChoices.COMPANY)
            elif type == str(TypeChoices.INT)[12:]:
                lst.append(TypeChoices.INT)
            elif type == str(TypeChoices.ADDRESS)[12:]:
                lst.append(TypeChoices.ADDRESS)
            elif type == str(TypeChoices.DATE)[12:]:
                lst.append(TypeChoices.DATE)

        return lst

    @staticmethod
    def name_valid(name):
        if isinstance(name, str):
            return name.title()
        else:
            return str(name)

    @staticmethod
    def exist_duplicate(name, user):
        status = Schema.query.filter_by(name=name, user=user).first()
        if status is None:
            return True
        return False


class SaveSchema:
    def __init__(self, schema_name, separator, column_list, user):
        self._schema_name = schema_name
        self._separator = separator
        self._column_list = column_list
        self._user = user

        self.__save_schema()
        self.__save_column()

    def __save_schema(self):
        count = Schema.query.filter_by(user=self._user).count()
        self.new_schema = Schema(name=self._schema_name, separate=self._separator, user=self._user, order=count+1)
        db.session.add(self.new_schema)
        db.session.commit()

    def __save_column(self):
        for block_column in self._column_list:
            new_column = ColumnSchema(name=block_column[0], type=block_column[1], schema_id=self.new_schema.id)
            db.session.add(new_column)
            db.session.commit()
