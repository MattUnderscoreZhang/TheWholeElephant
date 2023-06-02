import datetime


def today() -> str:
    date = datetime.date.today()
    return f"{date.year}-{date.month:02}-{date.day:02}"
