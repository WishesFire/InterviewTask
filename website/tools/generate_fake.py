import json
import string
import random
import datetime

"""
    DateFake:
        1. Name (first, last)
        2. Job 
        3. Email
        4. Domain Name
        5. Phone number
        6. Company name
        7. Integer code
        8. Address
        9. Date Registration
"""


class GenerateFake:
    @staticmethod
    def generate_name() -> str:
        name = ''
        for _ in range(2):
            name += "".join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 15))) + ' '
        return name[:-1]

    @staticmethod
    def generate_job() -> str:
        with open('fake/json/jobs.json') as f:
            data = json.load(f)
        job = random.choice(data.get('jobs'))[0]
        return job

    @staticmethod
    def generate_email() -> str:
        return "".join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 15))) + '.@email'

    @staticmethod
    def generate_domain() -> str:
        return "".join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 15))).title()

    @staticmethod
    def generate_phone_number() -> str:
        return '+' + "".join(str(random.randint(0, 9)) for _ in range(7))

    @staticmethod
    def generate_company_name() -> str:
        with open('fake/json/companies.json') as f:
            data = json.load(f)
        company = random.choice(data.get('companies'))[0]
        return company

    @staticmethod
    def generate_code() -> int:
        return random.randint(10000, 999999)

    @staticmethod
    def generate_address() -> str:
        with open('fake/json/addresses.json') as f:
            data = json.load(f)
        address = random.choice(data.get('addresses'))[0]
        return address

    @staticmethod
    def generate_date_registration() -> datetime:
        start = datetime.datetime.strptime("1/1/2020 00:00 AM", "%m/%d/%Y %I:%M %p")
        end = datetime.datetime.strptime("1/1/2021 12:00 AM", "%m/%d/%Y %I:%M %p")
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return start + datetime.timedelta(seconds=random_second)

    def control_panel(self, column_id):
        name = self.generate_name()
        job = self.generate_job()
        email = self.generate_email()
        domain = self.generate_domain()
        phone_number = self.generate_phone_number()
        company = self.generate_company_name()
        code = self.generate_code()
        address = self.generate_address()
        date = self.generate_date_registration()
