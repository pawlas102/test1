import datetime  # Standardowy moduł do pracy z datą i czasem
import json  # Standardowy moduł do kodowania/dekodowania JSON


def generuj_dane_o_systemie():
    """
    Generuje i wyświetla dane systemowe oraz aktualny czas,
    używając wyłącznie wbudowanych bibliotek Pythona.
    """

    # 1. Użycie modułu datetime do pobrania aktualnego czasu
    aktualny_czas = datetime.datetime.now()
    format_czasu = aktualny_czas.strftime("%Y-%m-%d %H:%M:%S")

    # 2. Utworzenie słownika z danymi
    dane = {
        "status": "OK",
        "timestamp": format_czasu,
        "opis_programu": "Prosta demonstracja użycia wbudowanych modułów datetime i json.",
        "liczba_pi": 3.14159,
        "lista_testowa": [10, 20, 30]
    }

    print("--- Surowe dane (Python dict) ---")
    print(dane)
    print("-" * 40)

    # 3. Użycie modułu json do konwersji słownika na czytelny JSON
    try:
        # json.dumps konwertuje obiekt Pythona (słownik) na ciąg JSON.
        # indent=4 sprawia, że JSON jest ładnie sformatowany (wcięty).
        json_output = json.dumps(dane, indent=4)

        print("\n--- Wyjście w formacie JSON (ciąg znaków) ---")
        print(json_output)

    except TypeError as e:
        print(f"❌ Wystąpił błąd podczas konwersji na JSON: {e}")


# Uruchomienie funkcji
generuj_dane_o_systemie()