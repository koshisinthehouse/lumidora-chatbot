from src.chatbot.agent import LumidoraAgent
from src.chatbot.chat import LumidoraChatbotConfiguration
from src.chatbot.lumidora import Lumidora
from langchain.output_parsers import ResponseSchema


def main():
    lumidora = Lumidora()
    lumidora.create_directories()
    lumidora.add_agent("Agent1")
    agent: LumidoraAgent | None = lumidora.get_agent("Agent1")
    if agent:
        print(f"Gefunden: {agent.name}")
        agent.open_agent_directory()
        agent.add_text(
            text=""" 22.12.2023: haninchin ist super. Er wird immer besser werden.                                                              24.12.2023: haninchin ist schlecht, ich denke er wird schlechter."""
        )
        agent.create_vectorstore()
        template = """
        Du bist ein hochqualifizierter Content-Ersteller, bekannt für die Produktion von viralen YouTube-Videos.
        Deine Aufgabe ist es, ansprechende und informative Inhalte zu erstellen, die mit der Zielgruppe resonieren und die Zuschauerbindung maximieren.
        Dein Video sollte SEO-optimiert sein, um das breiteste Publikum zu erreichen.
        Du dutzt dein Publikum
       
        context: {context}

        text: {question}

        {format_instructions}
        """
        model_path = "c:/_dev/models/mistral-7b-openorca.Q8_0.gguf"
        text_schemas: list[ResponseSchema] = []
        text_schemas.append(
            ResponseSchema(name="video_topic", description="the video headline")
        )
        text_schemas.append(
            ResponseSchema(name="keywords", description="main words in the video")
        )
        text_schemas.append(
            ResponseSchema(
                name="introduction",
                description="audience greeting, brief summary of the main topics, mention of the like button and subscription.",
            )
        )
        text_schemas.append(
            ResponseSchema(
                name="sentiment",
                description="What subject is the text about? Use exactly one word.",
            )
        )
        text_schemas.append(
            ResponseSchema(
                name="article",
                description="Article about the latest news about the topic",
            )
        )
        config = LumidoraChatbotConfiguration(
            model_path=model_path, template=template, text_schemas=text_schemas
        )
        text = "Gib mir Informationen zu haninchin aus"
        response = agent.question(text, config)
        print(response)
        # lumidora.remove_agent("Agent1")


if __name__ == "__main__":
    main()
