# Реализация интерактивной игры и взаимодействия с пользователем
import sys

from engine import HangmanGame
from game_session import GameSession
from interactive_methods import display_game_state
from interactive_methods import show_final_result
from interactive_methods import get_user_input
from interactive_methods import offer_hint
from interactive_methods import choose_category
from interactive_methods import choose_difficulty
from interactive_methods import automatic_word_choose
from constants.difficulty_settings import TIME_FOR_ANSWER
import time

def play_interactive():
    game_session = GameSession()
    print("Добро пожаловать в игру Виселица!\n")
    play = True # Сохраняем статус игровой сессии
    answers_list = [] # Сохраняем все ответы сыгранных игр, чтобы потом не повторить задание
    while play:
        category = choose_category()
        difficulty, max_errors = choose_difficulty()

        word, hint = automatic_word_choose(category)

        # Выбираем ещё не сыгранное слово
        iterations = 0
        while word in answers_list:
            word, hint = automatic_word_choose(category)
            iterations += 1
            # Если долго не можем подобрать новое слово - нужно подбирать новую категорию
            if iterations > 30:
                print("В выбранной категории закончились слова. Выберите, пожалуйста, другую.")
                category = choose_category()
                iterations = 0

        print("Начало игры")

        game = HangmanGame(word, max_errors)
        is_hint_offered = False
        start_time = time.time()

        while not game.is_over():
            display_game_state(game, category, difficulty)
            # Подсказку предлагаем, когда остается 1 шанс на ошибку
            is_hint_offered = offer_hint(hint, game.errors, max_errors - 2, is_hint_offered)

            start_timing = time.time()
            # Если не уложиться в 20 секунд, то ответ засчитан не будет
            guess_input = get_user_input()
            if time.time() - start_timing > TIME_FOR_ANSWER:
                print("Вы не уложились в 20 секунд, отведенные на ввод!")
                game.errors += 1
            else:
                is_correct = game.guess(guess_input)

                if is_correct:
                    print("Угадано верно!\n")
                else:
                    print("Не угадано.\n")

        if game.is_won():
            game.result = True
        elif game.is_lost():
            game.result = False

        show_final_result(game, word, difficulty)

        end_time=time.time()
        game.game_time = round(end_time - start_time, 2)

        # Вносим результат и добавляем штраф за использованную подсказку
        if is_hint_offered:
            game_session.result_add(game.answer, game.difficulty, game.result, game.game_time + 25, game.errors)
        else:
            game_session.result_add(game.answer, game.difficulty, game.result, game.game_time, game.errors)
        game_session.results_print()

        answers_list.append(game.answer) # Этот ответ больше не играем
        if len(answers_list) == 64:
            print("Вы сыграли со всеми возможными словами. Ваша игровая сессия окончена!")
            break

        choice = input("Хотите ли вы сыграть еще раз? Введите да, если хотите, или любой другой ввод для завершения.\n").strip().lower()
        if choice in ("да", "yes"):
            play = True
        else:
            play = False

    print("Игра окончена. Спасибо!")