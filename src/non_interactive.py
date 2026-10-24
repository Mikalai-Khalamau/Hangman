# Неинтерактивный режим: Функция сравнивает 2 слова, проверяет, что длины равны,
# возвращает маску и результат.

def compare_words(answer: str, guessed: str) -> str:
    # Учитываем регистр - сразу переводим все буквы в строчные
    answer = answer.lower()
    guessed = guessed.lower()

    if len(answer) != len(guessed):
        raise ValueError("Слова должны быть одинаковой длины")

    # В маску собираем те буквы, которые угадали, а также звездочки на месте неугаданных
    masked = ""
    for i in range(len(answer)):
        if answer[i] == guessed[i]:
            masked += answer[i]
        else:
            masked += "*"

    # Если угадываемое и предположенное совпали, то результат POS, иначе NEG
    if masked == answer:
        result_status = "POS"
    else:
        result_status = "NEG"

    # Возвращаем строку, состоящую из маски и результата
    return f"{masked};{result_status}"



