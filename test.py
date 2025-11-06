import pyfiglet  # Importujemy zainstalowaną bibliotekę


def generate_ascii_names():
    """
    Generuje i wyświetla imiona w formie ASCII art.
    """

    names = ["World", "James", "Jane", "Kirk"]  # Zmieniamy na same imiona, "hello" dodamy później

    print("----- Powitania w stylu ASCII Art -----")
    print("-" * 40)

    for name in names:
        # Tworzymy pełny tekst, który ma być przekształcony na ASCII art
        full_text = f"Hello {name}!"

        try:
            # Używamy pyfiglet.figlet_format do konwersji tekstu na ASCII art
            # Możesz eksperymentować z różnymi 'font' (np. 'slant', 'chunky', 'block')
            ascii_art = pyfiglet.figlet_format(full_text, font="standard")

            print(ascii_art)
            print("-" * 40)  # separator dla czytelności

        except Exception as e:
            print(f"❌ Błąd podczas generowania ASCII art dla '{full_text}': {e}")
            print("-" * 40)


# Uruchomienie funkcji
generate_ascii_names()