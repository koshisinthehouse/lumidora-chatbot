from pickle import FALSE
import gradio as gr
import requests


import json


class GradioApp:
    def fetch_and_play(self, text):
        my_object = {
            "text": text,
            "voice": "domoskanonos.onnx"
        }
        json_string = json.dumps(my_object)
        headers = {'Content-Type': 'application/json'}  # Setzen des Content-Types
        try:
            response = requests.post("http://localhost:7862/api/tts", data=json_string, headers=headers)
            response.raise_for_status()  # Dies löst eine Ausnahme bei HTTP-Fehlern aus
            return response.content
        except requests.exceptions.HTTPError as e:  # Spezifischer für HTTP-Fehler
            print(f"HTTP error occurred: {e}")  # HTTP-Fehlermeldung
            print(response.text)  # Text des Server-Responses ausgeben
            return None
        except requests.exceptions.RequestException as e:  # Dies fängt alle Anfrage-bezogenen Fehler
            print(f"An error occurred: {e}")
            return None

    def run(self):
        iface = gr.Interface(
            self.fetch_and_play, 
            inputs=[gr.TextArea(label="Text")], 
            outputs="audio"
        )
        
        iface.launch(server_port=7860, share=False)

