class NameLengthError(ValueError):
    def __init__(self, name):
        self.name = name
        message = f"Ім'я '{name}' занадто коротке (менше 10 символів)"
        super().__init__(message)


def task06():
    def check_name(name):
        if len(name) < 10:
            raise NameLengthError(name)

    try:
        check_name("Іван")
    except NameLengthError as error:
        print(f"{error}")

    try:
        check_name("Олександр")
    except NameLengthError as error:
        print(f"{error}")


task06()

