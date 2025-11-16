import re
from datetime import datetime, date

class Person:
    def __init__(self, surname, first_name, birth_date, nickname=None):
        regex_pattern = re.compile(r"^[A-Za-zА-Яа-яЇїІіЄєҐґ'-]+(?: [A-Za-zА-Яа-яЇїІіЄєҐґ'-]+)*$")

        if not isinstance(surname, str) or not surname.strip() or not regex_pattern.fullmatch(surname):
            raise ValueError("Поле 'surname' невалідне")
        self.surname = surname.strip()

        if not isinstance(first_name, str) or not first_name.strip() or not regex_pattern.fullmatch(first_name):
            raise ValueError("Поле 'first_name' невалідне")
        self.first_name = first_name.strip()

        if nickname is not None:
            if not isinstance(nickname, str) or not nickname.strip() or not re.fullmatch(r"^[A-Za-z0-9_-]+$", nickname):
                raise ValueError("Поле 'nickname' невалідне")
            self.nickname = nickname.strip()
        else:
            self.nickname = None

        if isinstance(birth_date, str):
            try:
                year, month, day = map(int, birth_date.split('-'))
                birth_date_obj = date(year, month, day)  # <- тут виправлено
            except ValueError:
                raise ValueError("Поле 'birth_date' невалідне")
        elif isinstance(birth_date, datetime):
            birth_date_obj = birth_date.date()
        else:
            raise ValueError("Поле 'birth_date' невалідне")

        if birth_date_obj > date.today():
            raise ValueError("Поле 'birth_date' невалідне: дата не може бути в майбутньому")

        self.birth_date = birth_date_obj

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1

        return age

    def full_name(self):
        return "%s %s" % (self.surname, self.first_name)
