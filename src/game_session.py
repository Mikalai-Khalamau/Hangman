# Класс сохраняет результаты всех попыток и определяет лучшую
class GameSession:
    def __init__(self):
        self.games_results = {}

    def result_add(self, word: str, difficulty: str, result: bool, game_time: float, errors: int):
    # Учитываем выиграна ли игра, количество допущенных ошибок и длину слова
    # Чем меньше итоговый счет, тем лучше результат
        if not result:
            if 1 <= len(word) <= 5: # Простое слово - значит ошибок меньше и добавим штрафа
                score = 100 + round(game_time + errors * 15 + 40, 2)
            elif 6 <= len(word) <= 9: # Среднее слово
                score = 100 + round(game_time + errors * 15 + 20, 2)
            else: # Сложное слово
                score = 100 + round(game_time + errors * 15, 2)
        else:
            if 1 <= len(word) <= 5:  # Простое слово
                score = round(game_time + errors * 15 + 40, 2)
            elif 6 <= len(word) <= 9:  # Среднее слово
                score = round(game_time + errors * 15 + 20, 2)
            else:  # Сложное слово
                score = round(game_time + errors * 15, 2)
        # В словарь добавляем ключ - слово, значение - кортеж с параметрами результата игры
        self.games_results[word] = difficulty, result, game_time, errors, score

    def results_print(self):

        length = len(self.games_results)
        results_list = list(self.games_results.items())

        # Определяем последний результат и лучший результат
        print(f"Результат последней игры:")
        if results_list[length - 1][1][1]:
            print(f"Победа! Отгадано слово {results_list[length - 1][0]}")
        else:
            print(f"Поражение. Не отгадано слово {results_list[length - 1][0]}")
        print(f"Уровень: {results_list[length - 1][1][0]}. Допущено ошибок: {results_list[length - 1][1][3]}")
        print(f"Время игры: {results_list[length - 1][1][2]}. Финальный счёт: {results_list[length - 1][1][4]}\n")

        sorted_results = sorted(results_list, key=lambda item: item[1][4])
        print(f"Лучший результат:")
        if sorted_results[0][1][1]:
            print(f"Победа! Отгадано слово {sorted_results[0][0]}")
        else:
            print(f"Поражение. Не отгадано слово {sorted_results[0][0]}")
        print(f"Уровень: {sorted_results[0][1][0]}. Допущено ошибок: {sorted_results[0][1][3]}")
        print(f"Время игры: {sorted_results[0][1][2]}. Финальный счёт: {sorted_results[0][1][4]}\n")



