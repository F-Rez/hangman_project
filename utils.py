#!/usr/bin/python3
"""Funciones auxiliares: archivo de títulos, validación y estado en consola."""
import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORDLIST_PATH = os.path.join(BASE_DIR, "wordlist.txt")
ACCENTS = str.maketrans("áéíóúü", "aeiouu")


def normalize(text):
    """Pasa el texto a minúsculas y quita tildes. La ñ se conserva."""
    return text.lower().translate(ACCENTS)


def get_random_word(path=WORDLIST_PATH):
    """Lee el archivo de títulos y devuelve uno al azar."""
    with open(path, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip()]

    if not words:
        raise ValueError("wordlist.txt está vacío")
    return random.choice(words)


def is_valid_letter(text):
    """Indica si el texto es exactamente una letra."""
    return len(text) == 1 and text.isalpha()


def show_status(game):
    """Muestra el título oculto, las letras probadas y los intentos."""
    guessed = ", ".join(sorted(game.guessed_letters)) or "ninguna"
    wrong = ", ".join(sorted(game.wrong_letters)) or "ninguna"
    print()
    print(f"Título: {game.display_progress()}")
    print(f"Letras adivinadas: {guessed}")
    print(f"Letras incorrectas: {wrong}")
    print(f"Intentos restantes: {game.remaining_attempts()}")
