from website import make_celery
import csv

celery = make_celery()


@celery.task()
def generate_fake_data(rows_count):
    # TODO генерація fakedate в csv
    pass
