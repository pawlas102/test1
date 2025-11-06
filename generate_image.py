from PIL import Image
import os  # <-- Dodajemy import modułu 'os'


def generate_simple_image(filename="generated/test_image.png", size=(200, 200), color="red"):
    """
    Tworzy prosty obraz w podanym kolorze i zapisuje go jako plik.
    Automatycznie tworzy folder docelowy 'generated', jeśli nie istnieje.
    """

    # 1. Wyodrębnienie katalogu z pełnej ścieżki
    # os.path.dirname("generated/test_image.png") zwróci "generated"
    output_dir = os.path.dirname(filename)

    # 2. Sprawdzenie i utworzenie katalogu
    if output_dir and not os.path.exists(output_dir):
        try:
            # os.makedirs tworzy katalogi rekurencyjnie (tworzy 'generated')
            os.makedirs(output_dir)
            print(f"📁 Utworzono brakujący katalog: '{output_dir}'")
        except OSError as e:
            # Ta sekcja zabezpiecza przed rzadkimi błędami uprawnień
            print(f"❌ Błąd podczas tworzenia katalogu '{output_dir}': {e}")
            return  # Przerywamy funkcję, jeśli katalog nie może być utworzony

    try:
        # Tworzenie nowego obrazu.
        img = Image.new('RGB', size, color)

        # 3. Zapisanie obrazu do pliku
        img.save(filename)

        print(f"✅ Obrazek utworzony pomyślnie!")
        print(f"Plik '{filename}' został zapisany.")
        print(f"Rozmiar: {size[0]}x{size[1]}, Kolor: {color}")

    except Exception as e:
        print(f"❌ Wystąpił błąd podczas generowania obrazu: {e}")


# Uruchomienie funkcji generującej obraz
generate_simple_image()