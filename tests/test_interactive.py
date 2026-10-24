from src.engine import HangmanGame

def test_initial_state():
    game = HangmanGame("шатер", 3)
    assert game.get_masked_word() == "_____"
    assert game.errors == 0
    assert not game.is_over() and not game.is_won() and not game.is_lost()

def test_correct_guess():
    game = HangmanGame("ложка", 5)
    assert game.guess("к") is True
    assert game.get_masked_word() == "___к_"

def test_incorrect_guess():
    game = HangmanGame("ложка", 5)
    assert game.guess("у") is False
    assert game.errors == 1

def test_repeated_letter():
    game = HangmanGame("слово", 5)
    game.guess("с")
    assert game.guess("с") is True  # уже угадана — не штрафуем
    assert game.errors == 0

def test_letter_is_many_times_in_word():
    game = HangmanGame("ананас",2)
    assert game.guess("а") is True
    assert game.get_masked_word() == "а_а_а_"

def test_win_condition():
    game = HangmanGame("вода",6)
    game.guess("в")
    game.guess("д")
    game.guess("н")
    game.guess("а")
    game.guess("о")
    assert game.is_won() and game.is_over()

def test_win_without_errors():
    game = HangmanGame("вода", 6)
    game.guess("в")
    game.guess("д")
    game.guess("а")
    game.guess("о")
    assert game.is_won() and game.is_over() and game.errors == 0

def test_lose_condition():
    game = HangmanGame("вода", 3)
    game.guess("в")
    game.guess("д")
    game.guess("щ")
    game.guess("з")
    game.guess("л")
    game.guess("у")
    assert game.is_lost() and game.is_over()

def test_errors_count():
    game = HangmanGame("карта",5)
    game.guess("в")
    game.guess("д")
    game.guess("а")
    game.guess("з")
    game.guess("р")
    assert game.get_remaining_errors() == 1
