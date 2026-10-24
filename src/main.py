import sys
from non_interactive import compare_words
from interactive_game import play_interactive

def main():
    # При запуске в неинтерактивном режиме передается 3 аргумента командной строки:
    # имя скрипта(у нас main.py) и 2 слова
    if len(sys.argv) == 3:
        try:
            output = compare_words(sys.argv[1], sys.argv[2])
            print(output)
        except ValueError as e:
            print(f"Неправильный ввод: {e}", file = sys.stderr)
            sys.exit(1) # Программа заканчивает работу с ошибкой
    else:
        play_interactive() # Запускаем интерактивный режим

if __name__ == "__main__":
    main()

