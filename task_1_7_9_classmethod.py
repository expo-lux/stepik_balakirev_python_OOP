from string import ascii_lowercase, digits
import re


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @classmethod
    def check_name(cls, name):
        return set(name) <= set(cls.CHARS_FOR_NAME + ' ') and len(name.split()) == 2

    @staticmethod
    def check_card_number(number):
        return True if re.match(r"\d{4}-\d{4}-\d{4}-\d{4}$", number) else False


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV D")
print(CardCheck.check_card_number("1234-5678-9012-0000-00"))
print(CardCheck.check_name("SERGEI BALAKIREV DD"))
