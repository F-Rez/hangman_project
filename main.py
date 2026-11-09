#!/usr/bin/python3
"""Punto de entrada del ahorcado: entrada del jugador y bucle del juego."""
from game import HangmanGame
from utils import get_random_word, is_valid_letter, normalize, show_status


def read_letter(game):
    """Pide datos hasta recibir una letra válida que no se haya probado."""
    while True:
        letter = normalize(input("Ingresa una letra: ").strip())
        if not is_valid_letter(letter):
            print("Entrada inválida: escribe una sola letra.")
        elif game.was_tried(letter):
            print(f"Ya probaste la letra '{letter}'. Elige otra.")
        else:
            return letter


def play(game):
    """Ejecuta el bucle del juego hasta la victoria o la derrota."""
    while not game.is_won() and not game.is_lost():
        show_status(game)
        letter = read_letter(game)

        if game.process_guess(letter):
            print(f"¡Bien! La letra '{letter}' está en el título.")
        else:
            print(f"La letra '{letter}' no está en el título.")

    show_status(game)
    if game.is_won():
        print(f"¡Ganaste! El título era: {game.word}")
    else:
        print(f"Fin del juego. El título era: {game.word}")


def main():
    """Elige el título, crea la partida y maneja los errores generales."""
    try:
        word = get_random_word()
    except FileNotFoundError:
        print("Error: no se encontró el archivo wordlist.txt.")
        return
    except ValueError:
        print("Error: wordlist.txt está vacío.")
        return

    print("=== AHORCADO ===")
    print("Adivina el título letra por letra. Pierdes con 6 errores.")

    try:
        play(HangmanGame(word))
    except (EOFError, KeyboardInterrupt):
        print("\nPartida cancelada.")


if __name__ == "__main__":
    main()
