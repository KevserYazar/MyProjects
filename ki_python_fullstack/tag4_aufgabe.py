" Mood Evaluator - Ein einfaches Programm zur Stimmungsauswertung "

# Firmen nutzen Docstrings oft zur automatischen Generierung von API-Dokumentationen

def evaluate_mood(mood: str) -> str:
    
    """
    Docstring für evaluate_mood
    
    :param mood: Beschreibung
    :type mood: str
    :return: Beschreibung
    :rtype: str
    """

""" Bewertet die eingegebene Stimmung und gibt eine entsprechende Nachricht zurück.  
 Args: 
            mood (str): Die Stimmung als String (z.B. 'gut', 'schlecht', 'traurig', 'glücklich')
        
        Returns:
            str:  Eine aufmunternde Nachricht bei negativer Stimmung oder 
                 eine bestätigende Nachricht bei positiver Stimmung
        
        Raises:
            ValueError:  Wenn mood leer oder nur Leerzeichen enthält
        
        Examples:
            >>> evaluate_mood("traurig")
            'Kopf hoch! 😊 Schlechte Zeiten gehen vorbei.  Du schaffst das!'
            
            >>> evaluate_mood("glücklich")
            'Das freut mich! 🎉 Behalte diese positive Energie!'
    """
    # Fehler werfen, wenn mood leer ist
    if not mood or mood.strip() == "":
        raise ValueError("Die Stimmung darf nicht leer sein!")
    
    # Normalisiere die Eingabe für Vergleich
    mood_lower = mood. lower().strip()
    
    # Definiere negative und positive Stimmungen
    negative_moods = ['schlecht', 'traurig', 'deprimiert', 'niedergeschlagen', 
                      'müde', 'gestresst', 'ängstlich', 'wütend', 'frustriert']
    
    positive_moods = ['gut', 'glücklich', 'fröhlich', 'begeistert', 'motiviert',
                      'zufrieden', 'entspannt', 'euphorisch', 'optimistisch']
    
    # Prüfe auf negative Stimmung
    if any(neg_mood in mood_lower for neg_mood in negative_moods):
        return ("Kopf hoch! 😊 Schlechte Zeiten gehen vorbei. "
                "Du schaffst das!  Denk daran:  Nach Regen kommt Sonnenschein!  🌈")
    
    # Prüfe auf positive Stimmung
    elif any(pos_mood in mood_lower for pos_mood in positive_moods):
        return ("Das freut mich! 🎉 Behalte diese positive Energie! "
                "Du bist auf dem richtigen Weg! ✨")
    
    # Neutrale oder unbekannte Stimmung
    else:
        return ("Danke, dass du deine Stimmung geteilt hast.  "
                "Ich hoffe, es geht dir gut! 💙")


def main():
    """
    Hauptfunktion zum Ausführen des Mood Evaluators. 
    Fordert den Benutzer zur Eingabe auf und zeigt die Bewertung an.
    """
    print("=" * 50)
    print("   Willkommen beim Mood Evaluator!  🌟")
    print("=" * 50)
    print()
    
    try:
        # Benutzereingabe
        user_mood = input("Wie ist deine Stimmung heute? ")
        
        # Stimmung bewerten
        result = evaluate_mood(user_mood)
        
        # Ergebnis anzeigen
        print()
        print("-" * 50)
        print(result)
        print("-" * 50)
        
    except ValueError as e:
        print(f"\n❌ Fehler: {e}")
        print("Bitte gib eine gültige Stimmung ein.")
    
    except KeyboardInterrupt:
        print("\n\nProgramm wurde beendet.  Bis bald! 👋")
    
    except Exception as e: 
        print(f"\n❌ Ein unerwarteter Fehler ist aufgetreten: {e}")


if __name__ == "__main__":
    main()  
