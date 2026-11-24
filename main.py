#!/usr/bin/env python3
"""The One-Line Exit — entry.

The letter is the entry's title on make.fun (exactly one line).
Running this prints the letter.
"""
LETTER = "I resign effective immediately, mostly because the office printer has seen me cry more times than HR ever has."

def letter():
    """Return the one-line resignation letter.

    One line, 110 characters, printer included.
    """
    return LETTER

def main():
    print(letter())

if __name__ == "__main__":
    main()
