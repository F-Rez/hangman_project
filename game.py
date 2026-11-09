#!/usr/bin/python3
"""Lógica del ahorcado. Este módulo no lee ni imprime nada."""
from utils import normalize


class HangmanGame:
    """Guarda el estado de una partida y aplica sus reglas."""

    def __init__(self, word):
        """Inicia una partida con el título que hay que adivinar."""
        self.word = word
        self.normalized_word = normalize(word)
        self.guessed_letters = []
        self.wrong_letters = []
        self.max_errors = 6
        self.errors = 0

    def was_tried(self, letter):
        """Indica si la letra ya se probó, acertada o no."""
        return letter in self.guessed_letters or letter in self.wrong_letters

    def process_guess(self, letter):
        """Registra una letra nueva y devuelve True si es correcta."""
        if letter in self.normalized_word:
            self.guessed_letters.append(letter)
            return True

        self.wrong_letters.append(letter)
        self.errors += 1
        return False

    def display_progress(self):
        """Devuelve el título con guiones bajos en las letras sin adivinar."""
        characters = []
        for original, normalized in zip(self.word, self.normalized_word):
            if not original.isalpha() or normalized in self.guessed_letters:
                characters.append(original)
            else:
                characters.append("_")
        return " ".join(characters)

    def remaining_attempts(self):
        """Devuelve cuántos errores más puede cometer el jugador."""
        return self.max_errors - self.errors

    def is_won(self):
        """Indica si ya se adivinaron todas las letras del título."""
        for character in self.normalized_word:
            if character.isalpha() and character not in self.guessed_letters:
                return False
        return True

    def is_lost(self):
        """Indica si se alcanzó el máximo de errores."""
        return self.errors >= self.max_errors
