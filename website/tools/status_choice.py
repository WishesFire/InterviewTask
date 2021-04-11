import enum


class TypeChoices(enum.Enum):
    NAME = 'full name'
    JOB = 'job'
    EMAIL = 'email'
    DOMAIN = 'domain'
    PHONE = 'phone'
    COMPANY = 'company'
    INT = 'integer'
    ADDRESS = 'address'
    DATE = 'date'

    CHOICES = (
        (NAME, 'Full name'),
        (JOB, "Job position"),
        (EMAIL, "E-mail"),
        (DOMAIN, 'Domain name'),
        (PHONE, "Phone number"),
        (COMPANY, 'Company name'),
        (INT, "Number range"),
        (ADDRESS, 'Address'),
        (DATE, "Date time"),
    )


FULL_LIST_CHOICE = ["JOB", "EMAIL", "DOMAIN", "PHONE", "COMPANY", "INT", "ADDRESS", "DATE"]


class StatusChoices(enum.Enum):
    READY = "ready"
    PROCESSING = "processing"
    FAILED = "failed"

    CHOICES = (
        (READY, "Готов к скачиванию"),
        (PROCESSING, "В работе"),
        (FAILED, "Ошибка"),
    )
