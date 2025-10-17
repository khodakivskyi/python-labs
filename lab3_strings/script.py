import re


def task01():
    while True:
        text = input("Введіть текст (до 1000 слів українською): ").strip()

        if not text:
            print("Помилка: рядок порожній.")
            continue

        if not re.search(r"[А-Яа-яЇїІіЄєҐґA-Za-z]", text):
            print("Помилка: ввід має містити текст.")
            continue

        words = re.findall(r"[А-Яа-яЇїІіЄєҐґA-Za-z']+", text)
        if len(words) > 1000:
            print("Помилка: текст містить більше ніж 1000 слів.")
            continue

        break

    while True:
        search_word = input("Введіть слово, з якого мають починатися інші слова: ").strip()
        if not search_word.isalpha():
            print("Помилка: пошукове слово має містити лише літери.")
            continue

        break

    pattern = rf"\b{re.escape(search_word)}[А-Яа-яЇїІіЄєҐґA-Za-z']*"
    found = re.findall(pattern, text, re.IGNORECASE)

    print(f"Кількість слів, що починаються з '{search_word}': {len(found)}")


def task02():
    while True:
        text = input("Введіть текст: ").strip()

        if not text:
            print("Помилка: рядок порожній.")
            continue

        if not re.search(r"[А-Яа-яЇїІіЄєҐґA-Za-z]", text):
            print("Помилка: ввід має містити текст.")
            continue

        break

    count_replacements = text.count('a')
    newText = text.replace('a', 'A')

    print("Рядок після заміни:", newText)
    print("Кількість замін:", count_replacements)

    print("Кількість символів:", len(newText))

    letters = sum(1 for char in newText if char.isalpha())
    print("Кількість літер:", letters)


def task03():
    while True:
        text = input("Введіть текст: ").strip()
        if not text:
            print("Помилка: рядок порожній.")
            continue
        if not re.search(r"[А-Яа-яЇїІіЄєҐґA-Za-z]", text):
            print("Помилка: текст має містити літери.")
            continue
        break

    while True:
        search_word = input("Введіть слово для пошуку: ").strip()
        if not search_word.isalpha():
            print("Помилка: слово має містити лише літери.")
            continue
        break

    pattern = rf"\b{re.escape(search_word)}[А-Яа-яЇїІіЄєҐґA-Za-z']*\b"
    matches = re.findall(pattern, text, re.IGNORECASE)

    print(f"Слово '{search_word}' зустрічається {len(matches)} раз(и).")


def task04():
    while True:
        text = input("Введіть текст (до 1000 слів українською): ").strip()
        if not text:
            print("Помилка: рядок порожній.")
            continue
        if not re.search(r"[А-Яа-яЇїІіЄєҐґA-Za-z]", text):
            print("Помилка: ввід має містити текст.")
            continue

        words = re.findall(r"[А-Яа-яЇїІіЄєҐґA-Za-z']+", text)
        if len(words) > 1000:
            print("Помилка: текст містить більше ніж 1000 слів.")
            continue
        break

    half_index = len(words) // 2

    first_half_words = words[:half_index]
    second_half_words = words[half_index:]

    first_half_words = [w.capitalize() for w in first_half_words]

    second_half_words = [w.lower() + '*' for w in second_half_words]

    tokens = re.findall(r"\w+|[^\w\s]", text, re.UNICODE)

    new_tokens = []
    word_count = 0
    for tok in tokens:
        if re.match(r"\w+", tok):
            if word_count < half_index:
                new_tokens.append(first_half_words[word_count])
            else:
                new_tokens.append(second_half_words[word_count - half_index])
            word_count += 1
        else:
            new_tokens.append(tok)

    insert_index = len(new_tokens) // 2
    new_tokens.insert(insert_index, '|')

    final_text = ''
    for i, tok in enumerate(new_tokens):
        if re.match(r"\w+|\*", tok):
            final_text += tok + ' '
        else:
            final_text += tok

    print("Рядок після обробки:")
    print(final_text.strip())


def task05():
    while True:
        text = input("Введіть текст (до 1000 слів англійською): ").strip()
        if not text:
            print("Помилка: рядок порожній.")
            continue
        if not re.fullmatch(r"[A-Za-z\s,.!?']+", text):
            print("Помилка: ввід має містити англійський текст.")
            continue

        words = re.findall(r"[A-Za-z']+", text)
        if len(words) > 1000:
            print("Помилка: текст містить більше ніж 1000 слів.")
            continue
        break

    while True:
        start_letter = input("Введіть літеру, з якої мають починатися слова: ").strip()
        if len(start_letter) == 1 and re.fullmatch(r"[A-Za-z]", start_letter):
            start_letter = start_letter.upper()
            break
        else:
            print("Помилка: введіть одну англійську літеру.")

    while True:
        end_letter = input("Введіть літеру, на яку мають закінчуватися слова: ").strip()
        if len(end_letter) == 1 and re.fullmatch(r"[A-Za-z]", end_letter):
            end_letter = end_letter.upper()
            break
        else:
            print("Помилка: введіть одну англійську літеру.")

    words = re.findall(r"[A-Za-z]+", text)
    print("Слова, які починаються на", start_letter, "або закінчуються на", end_letter, ":")
    count = 0
    for word in words:
        if word[0].upper() == start_letter and word[len(word)-1].upper() == end_letter:
            print(word)
            count += 1

    if count == 0:
        print("Потрібних слів не знайдено")


def task06():
    while True:
        text = input("Введіть текст (до 100 слів англійською): ").strip()
        if not text:
            print("Помилка: рядок порожній.")
            continue
        if not re.fullmatch(r"[A-Za-z\s,.!?']+", text):
            print("Помилка: ввід має містити англійський текст.")
            continue

        words = re.findall(r"[A-Za-z']+", text)
        if len(words) > 1000:
            print("Помилка: текст містить більше ніж 100 слів.")
            continue
        break

    vowels = "aeiouAEIOU"

    count = sum(1 for char in text if char in vowels)

    print(f"Кількість голосних літер у тексті: {count}")


# def task07():