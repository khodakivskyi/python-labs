import re


def validate_text(max_words=None, language='any', prompt="Введіть текст: "):
    while True:
        text = input(prompt).strip()

        if not text:
            print("Помилка: рядок порожній.")
            continue

        if language == 'eng':
            if not re.fullmatch(r"[A-Za-z\s,.!?';:-]+", text):
                print("Помилка: ввід має містити англійський текст.")
                continue
            words = re.findall(r"[A-Za-z']+", text)
        elif language == 'ukr':
            if not re.search(r"[А-Яа-яЇїІіЄєҐґ]", text):
                print("Помилка: ввід має містити український текст.")
                continue
            words = re.findall(r"[А-Яа-яЇїІіЄєҐґA-Za-z']+", text)
        else:
            if not re.search(r"[А-Яа-яЇїІіЄєҐґA-Za-z]", text):
                print("Помилка: ввід має містити текст.")
                continue
            words = re.findall(r"[А-Яа-яЇїІіЄєҐґA-Za-z']+", text)

        if max_words and len(words) > max_words:
            print(f"Помилка: текст містить більше ніж {max_words} слів.")
            continue

        return text


def validate_word(prompt="Введіть слово: "):
    while True:
        word = input(prompt).strip()
        if word.startswith("'"):
            print("Помилка: слово не може починатися з апострофа.")
            continue
        if not re.match(r"^[А-Яа-яЇїІіЄєҐґA-Za-z']+$", word):
            print("Помилка: слово має містити лише літери (можливі апострофи).")
            continue
        return word

def validate_letter(language='eng', prompt="Введіть літеру: "):
    while True:
        letter = input(prompt).strip()

        if language == 'eng':
            if len(letter) == 1 and re.fullmatch(r"[A-Za-z]", letter):
                return letter.upper()
            else:
                print("Помилка: введіть одну англійську літеру.")
        else:
            if len(letter) == 1 and re.fullmatch(r"[А-Яа-яЇїІіЄєҐґ]", letter):
                return letter.upper()
            else:
                print("Помилка: введіть одну українську літеру.")


# tasks
def task01():
    text = validate_text(max_words=1000, language='ukr', prompt="Введіть текст (до 1000 слів українською): ")
    search_word = validate_word("Введіть слово, з якого мають починатися інші слова: ")

    pattern = rf"\b{re.escape(search_word)}[А-Яа-яЇїІіЄєҐґA-Za-z']*"
    found = re.findall(pattern, text, re.IGNORECASE)

    print(f"Кількість слів, що починаються з '{search_word}': {len(found)}")


def task02():
    text = validate_text(language='ukr', prompt="Введіть текст: ")

    count_replacements = text.count('а')
    newText = text.replace('а', 'А')

    print("Рядок після заміни:", newText)
    print("Кількість замін:", count_replacements)
    print("Кількість символів:", len(newText))

    letters = sum(1 for char in newText if char.isalpha())
    print("Кількість літер:", letters)


def task03():
    text = validate_text(language='any', prompt="Введіть текст: ")
    search_word = validate_word("Введіть слово для пошуку: ")

    pattern = rf"\b{re.escape(search_word)}\b"
    matches = re.findall(pattern, text, re.IGNORECASE)

    print(f"Слово '{search_word}' зустрічається {len(matches)} раз(и).")


def task04():
    text = validate_text(max_words=1000, language='ukr', prompt="Введіть текст (до 1000 слів українською): ")

    words_with_pos = [(m.group(), m.start(), m.end()) for m in re.finditer(r"[А-Яа-яЇїІіЄєҐґA-Za-z']+", text)]
    half_index = len(words_with_pos) // 2

    if not words_with_pos:
        print("Текст не містить слів!")
        return

    result = ""
    last_pos = 0

    for i, (word, start, end) in enumerate(words_with_pos):
        result += text[last_pos:start]

        if i == half_index:
            result += '| '

        if i < half_index:
            result += word.capitalize()
        else:
            result += word.lower() + '*'

        last_pos = end

    result += text[last_pos:]

    print("Рядок після обробки:")
    print(result)


def task05():
    text = validate_text(max_words=1000, language='eng', prompt="Введіть текст (до 1000 слів англійською): ")
    start_letter = validate_letter(language='eng', prompt="Введіть літеру, з якої мають починатися слова: ")
    end_letter = validate_letter(language='eng', prompt="Введіть літеру, на яку мають закінчуватися слова: ")

    words = re.findall(r"[A-Za-z]+", text)

    start_words = [word for word in words if word[0].upper() == start_letter]
    end_words = [word for word in words if word[-1].upper() == end_letter]

    print(f"\nСлова, які починаються на '{start_letter}':")
    if start_words:
        for word in start_words:
            print(word)
        print(f"Знайдено: {len(start_words)}")
    else:
        print("Не знайдено")

    print(f"\nСлова, які закінчуються на '{end_letter}':")
    if end_words:
        for word in end_words:
            print(word)
        print(f"Знайдено: {len(end_words)}")
    else:
        print("Не знайдено")


def task06():
    text = validate_text(max_words=100, language='eng', prompt="Введіть текст (до 100 слів англійською): ")

    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)

    print(f"Кількість голосних літер у тексті: {count}")


def task07():
    text = validate_text(max_words=1000, language='eng', prompt="Введіть англійський текст (до 1000 слів): ")

    sentences = re.split(r'[.!?]+', text)

    proper_nouns = []
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        words_in_sentence = re.findall(r"\b[A-Z][a-z']*\b", sentence)

        if len(words_in_sentence) > 1:
            proper_nouns.extend(words_in_sentence[1:])

    print("\nСлова з великої літери (імена та власні назви):")
    if proper_nouns:
        print(proper_nouns)
    else:
        print("Не знайдено слів, що починаються з великої літери.")


task01()