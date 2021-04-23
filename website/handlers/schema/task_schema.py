from celery import Celery
from website.tools.generate_fake import GenerateFake
from website.database.models_schema import FileSchema, Schema
from website import db
from io import StringIO
import csv
from dotenv import load_dotenv
import os

load_dotenv()


celery = Celery(__name__)
celery.conf.broker_url = os.getenv('CELERY_BROKER_URL')
celery.conf.result_backend = os.getenv('CELERY_RESULT_BACKEND')


@celery.task(name="create_generator_fake_task")
def generate_fake_data(rows_count, separator, user, schema_id):
    try:
        all_columns = Schema.query.filter_by(id=schema_id, user=user).first()
        all_columns_prepare = [column_type for column_type in all_columns.columns]
        buffer_memory = StringIO()
        buffer_memory.seek(0)

        writer = csv.writer(buffer_memory, quotechar=separator)
        schema_column_preparing = [column.name for column in all_columns_prepare]
        schema_column_types = [column.type for column in all_columns_prepare]
        writer.writerow(schema_column_preparing)
        for _ in range(rows_count + 1):
            for column_type in schema_column_types:
                writer.writerow(GenerateFake().control_panel(column_type))

        finally_file = buffer_memory.getvalue().encode('utf-8')
        status = "READY"
    except Exception as exc:
        print(exc)
        status = "FAILED"
        save_file(status, schema_id, user)
        return False
    else:
        save_file(status, schema_id, user, finally_file)
        buffer_memory.close()

    return True


def save_file(status, schema_id, user, file=None):
    if file:
        new_file = FileSchema(status=status, file=file, schema=schema_id, user=user)
    else:
        new_file = FileSchema(status=status, schema=schema_id, user=user)
    db.session.add(new_file)
    db.session.commit()
