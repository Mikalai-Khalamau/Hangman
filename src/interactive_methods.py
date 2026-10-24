from constants.words import CATEGORIES
from constants.words import RUSSIAN_ALPHABET
from constants.difficulty_settings import DIFFICULTY_LEVELS
from constants.hangman_stages_renderer import HANGMAN_STAGES
from engine import HangmanGame
import random

def choose_difficulty() -> tuple[str, int]:
    print("Доступные уровни сложности:\n")
    levels_list = list(DIFFICULTY_LEVELS.keys())
    for i in range (0, len(levels_list)):
        level = levels_list[i]
        print(f"{i + 1}. {level}, допустимых ошибок: {DIFFICULTY_LEVELS[level] - 1}")

    choice = input("\nВыберите уровень сложности из списка или выполните любой другой ввод для случайного выбора:\n")
    if choice.isdigit() and 1 <= int(choice) <= len(levels_list):
        selected = levels_list[int(choice) - 1]
        print(f"Выбран уровень: {selected}\n")
    else:
        selected = random.choice(levels_list)
        print(f"Выбран случайный уровень: {selected}\n")
    return selected, DIFFICULTY_LEVELS[selected]

def choose_category() -> str:
    print("Список доступных категорий:")
    categories_list = list(CATEGORIES.keys())
    for i in range (0, len(categories_list)):
        category = categories_list[i]
        print(f"{i + 1}. {category}")

    choice = input("\nВыберите номер категории из списка или выполните любой другой ввод для случайного выбора:\n")
    if choice.isdigit() and 1 <= int(choice) <= len(categories_list):
        selected = categories_list[int(choice) - 1]
        print(f"Выбрана категория: {selected}\n")
    else:
        selected = random.choice(categories_list)
        print(f"Выбрана случайная категория: {selected}\n")
    return selected

def automatic_word_choose(category: str) -> tuple[str, str]:
    words_for_category_list = list(CATEGORIES[category].keys())
    word = random.choice(words_for_category_list)
    hint = CATEGORIES[category][word]
    return word, hint

def display_game_state(game: HangmanGame,category: str, difficulty: str) -> None:
    errors_for_lose = DIFFICULTY_LEVELS[difficulty]
    display_hangman(game, errors_for_lose)
    print(f"Категория: {category}")
    print(f"Уровень: {difficulty}")
    print(f"Осталось допустимых ошибок: {game.get_remaining_errors()}")
    print(f"Уже введенные буквы: {list(game.entered_letters)}")
    print(f"Слово: {game.get_masked_word()}\n")

def display_hangman(game: HangmanGame, errors_for_lose: int) -> None:
    if game.is_lost():
        print(HANGMAN_STAGES[8])
    else:
        # Рисуем интервально, учитывая сложность, т.е. количество ошибок, при которых наступит проигрыш
        stage_index = min(8, round((game.errors / errors_for_lose) * 8))
        print(HANGMAN_STAGES[stage_index])

def show_final_result(game: HangmanGame, answer: str, difficulty: str):
    display_hangman(game, DIFFICULTY_LEVELS[difficulty])
    if game.is_won():
        print(f"Игра завершена. Вы угадали слово {answer.upper()} и победили!")
    else:
        print(f"Игра завершена. Вы не угадали слово {answer.upper()} и проиграли!")

def get_user_input() -> str:
    while True:
        word = input("Пожалуйста, введите букву(либо слово целиком, но без возможности ошибки):\n").strip().lower()
        if len(word) == 1:
            letter = word
            if letter.isalpha() and letter in RUSSIAN_ALPHABET:
                return letter
        else: # Побуквенная проверка корректности введенного целого слова
            good_letters = 0
            for letter in word:
                if letter.isalpha() and letter in RUSSIAN_ALPHABET:
                    good_letters += 1
            if good_letters == len(word):
                return word


def offer_hint(hint: str, errors: int, max_for_hint: int, is_hint_offered : bool):
    if is_hint_offered:
        return True
    if errors >= max_for_hint and not is_hint_offered:
        choice = input("Введите да, если хотите взять подсказку\n").strip().lower()
        if choice in ("да", "yes"):
            print(f"Подсказка: {hint}\n")
            return True
    return None