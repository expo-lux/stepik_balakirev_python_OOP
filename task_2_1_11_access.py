from string import ascii_lowercase, digits
import random


class EmailValidator():
    CHARS_CORRECT = set(ascii_lowercase + digits)
    CHARS_CORRECT_AT = set(ascii_lowercase + ascii_lowercase.upper() + digits + '_' + '.' + '@')

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        Flag = False
        if cls.__is_email_str(email):
            before_at = email.split('@')[0]
            after_at = email.split('@')[1]
            if set(email) <= cls.CHARS_CORRECT_AT:
                if len(before_at) <= 100 and len(after_at) <= 50 and '.' in after_at and not '..' in email:
                    Flag = True
        return Flag

    @classmethod
    def get_random_email(cls):
        """генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com
        x - любой допустимый символ: латинский алфавит, цифры, символы подчеркивания, точки"""
        return ''.join(random.sample(cls.CHARS_CORRECT,15)) + '@gmail.com'

    @staticmethod
    def __is_email_str(email):
        return type(email) == str

res = EmailValidator.check_email("sc_lib@list.ru") # True
print(res)
res = EmailValidator.check_email("sc_lib@list_ru") # False
print(res)
res = EmailValidator.check_email("sclib@list.ru")
print(res)
res = EmailValidator.check_email("sc.lib@listru")
print(res)
res = EmailValidator.check_email("sc..lib@list.ru")
print(res)