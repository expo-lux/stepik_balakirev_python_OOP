from datetime import datetime


class DateError(Exception):
    def __str__(self):
        return "Неверный формат даты"


class DateSting:
    def __init__(self, date: str):
        try:
            self.date = datetime.strptime(date, '%d.%m.%Y').strftime('%d.%m.%Y')
        except ValueError:
            raise DateError()

    def __str__(self):
        return self.date


# date_string = input()
date_string = "01.xx.2000"
try:
    print(DateSting(date_string))
except DateError as e:
    print(e)
