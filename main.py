import os


def maikn():
    print("Chatbot")

    # Specify the model path
    model_path = "C:/_dev/repositories/Lumidora/resources/llm/resources/mistral-7b-openorca.Q4_0.gguf"



from src.chatbot.ui.iface import GradioApp

from src.chatbot.lumidora import Lumidora


import uvicorn


import threading

import tempfile


def prepare():
    temp_path = tempfile.gettempdir()
    print("Temporäres Verzeichnis:", temp_path)
    # Pfad für den neuen Unterordner erstellen
    app_temp_dir = os.path.join(temp_path, "Lumidora")
    # Unterordner erstellen, wenn er nicht bereits existiert
    if not os.path.exists(app_temp_dir):
        os.makedirs(app_temp_dir)
        print(f"Unterordner erstellt: {app_temp_dir}")
    else:
        print(f"Unterordner existiert bereits: {app_temp_dir}")
    

def main():
    

    lumidora = Lumidora()
    lumidora.create_directories()
    lumidora.add_agent("Agent1")
    agent = lumidora.get_agent("Agent1")
    if agent:
        print(f"Gefunden: {agent.name}")
    agent.open_agent_directory()
    
       
    agent.add_text(text="""
                   
                   
                   Bitcoin-Prognosen – das Wichtigste vorweg
Bitcoin (BTC) ist die erste und bekannteste Kryptowährung und wird oft als Benchmark für den Kryptowährungsmarkt verwendet. Sie wurde von einer anonymen Person oder Gruppe von Personen unter dem Pseudonym Satoshi Nakamoto geschaffen und in einem 2008 veröffentlichten Whitepaper vorgestellt.
Die Kryptowährung Bitcoin ist eine dezentralisierte digitale Währung, die auf einer Technologie namens Blockchain basiert. Im sogenannten Ledger (Hauptbuch) werden alle Transaktionen weltweit verteilt in einem Netzwerk von Computern aufzeichnet.
Das Kryptowährungspaar BTC/USD stellt den Wechselkurs zwischen Bitcoin (BTC) und dem US-Dollar (USD) dar. Dieses Paar wird häufig für den Handel verwendet und ist ein wichtiger Maßstab für die Beurteilung des Wertes von Bitcoin in traditioneller Währung.
Der BTC-Kurs in USD kann sehr volatil sein und wird von verschiedenen Faktoren beeinflusst, darunter Marktstimmung, Akzeptanz, regulatorische Entwicklungen und makroökonomische Bedingungen.
Bitcoin wird oft als Wertaufbewahrungsmittel, als digitales Gold und als mögliche Absicherung gegen Inflation angesehen. Er hat als Anlageobjekt an Beliebtheit gewonnen und wird für Transaktionen sowie als Mittel zur grenzüberschreitenden Wertübertragung verwendet.
Das bisherige Allzeithoch hat der Bitcoin im November 2021 bei 69.000 USD erreicht, sein letztes lokales Tief im November 2022 bei $15.476.
Hinweis: Die aufgeführten Szenarien entstehen aus meiner persönlichen Einschätzung und Erfahrung. Sie stellen eine Zusammenfassung der wahrscheinlichsten Kursspanne für die jeweilige Zeiteinheit dar. Handeln Sie angemessene Positionsgrößen nach Ihrem individuellen Risikomanagement. Trading im volatilen Krypto-Markt ist aufgrund der stärkeren Kursschwankungen wesentlich riskanter als im Forex- oder Aktien-Markt.
               
               Die argentinische Außenministerin Diana Mondino gab bekannt, dass ab sofort eine neue Regelung die legale Verwendung von Bitcoin in bestimmten rechtlichen Transaktionen ermöglicht. In einem entsprechenden Beitrag auf X bestätigte Mondino, dass die Verordnung, die auf wirtschaftliche Reformen und Deregulierung abzielt, in spezifischen Fällen die Verwendung von Bitcoin und anderer Kryptowährungen als Zahlungsmittel vorsieht. 

Die Verordnung mit dem Titel „Grundlagen für den Wiederaufbau der argentinischen Wirtschaft“ wurde am 20. Dezember verabschiedet. Obwohl Kryptowährungen im zugehörigen Entwurf nicht explizit genannt wurden, gelten entsprechende Bestimmungen für sie, die sich auf die Verwendung von Währungen beziehen, die kein gesetzliches Zahlungsmittel in Argentinien sind. „Wir ratifzieren und bestätigten, dass in Argentinien Geschäftsverträge ab sofort mit Bitcoin gezahlt werden können“, wie Mondino dahingehend verdeutlicht. „Das gilt auch für andere Kryptowährungen“, so Außenministerin Mondino weiter.

Bitcoin legte am Freitagmorgen leicht zu und stieg erneut kurzfristig über die 44.000-Dollar-Marke. Zuletzt notierte der Kurs der ältesten Kryptowährung laut dem Analysehaus Coinmarketcap bei 43.932,59 Dollar (Stand: 8:18 Uhr). Damit verzeichnete Bitcoin seit Jahresbeginn ein Kursplus von mehr als 164 Prozent.
    
                   
                   """,destination="temp")
    
    
    
    
    
    config_json = """
    {
        "model_path": "D:/Lumidora/resources/llm/resources/openchat_3.5.Q4_K_M.gguf",
        "template": "You are an employee of a professional translation agency and receive a text in German. You are asked to translate this text into perfect English. Here is the German text you have to translate: {input} . Output information: {format_instructions}",
        "text_schemas": [
            {
                "name": "translation",
                "description": "The translated text"
            }
        ]
    }
    """

    text = "Generiere eine hochwertige und realistische Illustration einer Comicfigur, die als Grundlage für künstliche Intelligenz auf einem YouTube-Kanal dienen soll. Die Figur soll eine fröhliche und freundliche Ausstrahlung haben, gepaart mit einem charismatischen Erscheinungsbild."
    
    response = agent.question(text, config_json)
    print(response)

    
    #lumidora.remove_agent("Agent1")


    prepare()
    #vec = LumidoraVectorDB()


    #app = GradioApp()
    #app.run()


# Pfad des temporären Verzeichnisses erhalten


    #uvicorn.run("src.chatbot.api.fastapi:app", host="0.0.0.0", port=8000, reload=True)
    #print("api started.")
    
    
    #print("Vektor")

    #device = 'cuda' if torch.cuda.is_available() else 'cpu'
    #print(f"Verwendetes Gerät: {'cuda'}")

        # Initialisieren Sie das Modell mit GPU-Unterstützung
    #model = HuggingfaceModel('gpt2').to(device)

    
    # Create an instance of the Chatbot class
    #vec = LumidoraVectorDB("C:/_dev/repositories/Lumidora/resources/llm/resources/mistral-7b-openorca.Q4_0.gguf", "")
    #vec = LumidoraVectorDB("./vector_db.faiss")
    #vec.create_vector_db("./datastore")

    # Define template and input text

    

    # Run the chat using the defined template and input text
    

if __name__ == "__main__":
    main()