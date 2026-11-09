# Ahorcado en Python

Juego del ahorcado para consola. El programa elige al azar un título de película de `wordlist.txt` y el jugador debe adivinarlo letra por letra antes de cometer 6 errores.

## Requisitos

Python 3.6 o superior. No necesita librerías externas.

## Cómo jugar

Desde la carpeta `hangman_project/`:

```bash
python3 main.py
```

## Reglas

- Se ingresa una sola letra por turno.
- Cada letra incorrecta suma un error.
- Con 6 errores, el jugador pierde.
- El jugador gana cuando adivina todas las letras del título.
- Una letra ya probada se rechaza y se vuelve a pedir, sin sumar error.
- Los espacios, números y signos de puntuación se revelan automáticamente.
- Las tildes no cuentan: la `a` también revela la `á`. La `ñ` es una letra distinta de la `n`.

## Estructura

```text
hangman_project/
├── main.py        # Inicio del programa, entrada del jugador y bucle del juego
├── game.py        # Clase HangmanGame con la lógica y las reglas
├── utils.py       # Selección del título, validación y estado en consola
├── wordlist.txt   # Títulos disponibles, uno por línea
└── README.md      # Descripción e instrucciones
```

## Agregar títulos

Escribe cada título nuevo en una línea de `wordlist.txt`. El archivo debe estar guardado en UTF-8.

## Autores
- Felipe Rezende
