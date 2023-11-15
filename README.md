# lumidora-chatbot
chatbot based on gpt4all


# useful python commands
## poetry

### install poetry
    pip install poetry

### Poetry Konfiguration anzeigen
    poetry config --list

### Projet initialisieren
    poetry init

### Virtuelle Umgebung erstellen
    # System Python Version verwenden
    poetry shell
    # Mit spezieller python version
    poetry env use D:/_dev/extract/python/python.exe

### Info über die Virtuelle Umgebung
    poetry env info

### Poetry Projekt initial installieren
     poetry install

### Dependency hinzufügen
    poetry add [package]

### Dev Dependency
    poetry add [package] --group dev

### Script starten
    poetry run cmd

### requrements.txt erzeugen
    poetry export -f requirements.txt --output requirements.txt



