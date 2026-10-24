# Класс сохраняет состояние одной попытки игры и реализует функции угадывания и вывода маски
class HangmanGame:
    def __init__(self, answer: str, errors_for_lose: int):
        self.answer = answer.lower()

        # Количество ошибок, приводящих к поражению. Зависит от уровня сложности
        self.errors_for_lose = errors_for_lose
        self.errors = 0
        self.entered_letters = []
        self.game_time = 0
        self.result = False

        self.difficulty = ""
        if self.errors_for_lose == 8:
            self.difficulty = "Лёгкий"
        elif self.errors_for_lose == 6:
            self.difficulty = "Средний"
        else:
            self.difficulty = "Сложный"

    def guess(self, user_input: str) -> bool:
        user_input = user_input.lower()
        # Ввели одну букву
        if len(user_input) == 1:
            letter = user_input
            if letter in self.entered_letters:
                # Букву уже вводили - выведем есть ли она в ответе, не добавляем ошибку
                return letter in self.answer

            self.entered_letters.append(letter)
            if letter in self.answer:
                return True
            else:
                self.errors += 1
                return False
        # Если попытались угадать целое слово
        elif len(user_input) == len(self.answer):
            good_letters = 0
            # Проверяем введенные буквы по одной и если все верны - победа пользователя
            for i in range(0, len(user_input)):
                self.entered_letters.append(user_input[i])
                if user_input[i] == self.answer[i]:
                    good_letters += 1

            if good_letters == len(self.answer):
                self.is_won()
                self.is_over()
                return True
            # При неправильной попытке угадать слово даем максимальный штраф и поражение
            else:
                self.errors = self.errors_for_lose + 1
                self.is_lost()
                self.is_over()
                return False
        # Если ввели букв не на целое слово, но и не одну букву - дадим ввести еще раз, не поражение
        else:
            return False

    def get_masked_word(self) -> str:
        masked_word = ""
        for letter in self.answer:
            if letter in self.entered_letters:
                masked_word += letter
            else:
                masked_word += "_"
        return masked_word

    def is_won(self) -> bool:
        return self.answer == self.get_masked_word()

    def is_lost(self) -> bool:
        return self.errors >= self.errors_for_lose

    def get_remaining_errors(self) -> int:
        return self.errors_for_lose - self.errors - 1

    def is_over(self) -> bool:
        return self.is_won() or self.is_lost()