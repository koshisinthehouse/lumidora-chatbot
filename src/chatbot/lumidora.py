import os
import shutil
import tempfile
from typing import Optional
from src.chatbot.agent import LumidoraAgent

class Lumidora:
    def __init__(self):
        self.base_temp_dir:str = tempfile.gettempdir()
        self.lumidora_dir:str = os.path.join(self.base_temp_dir, "Lumidora")
        self.agent_dir:str = os.path.join(self.lumidora_dir, "Agents")
        self.agents: list[LumidoraAgent] = []
        self.scan_and_create_agents()

    def scan_and_create_agents(self):
        # Make sure directories exist or are created
        self.create_directories()

        # Scan the agent directory for subdirectories
        for item in os.listdir(self.agent_dir):
            item_path = os.path.join(self.agent_dir, item)
            if os.path.isdir(item_path):
                # Check if the agent already exists to avoid duplicates
                if not any(agent.name == item for agent in self.agents):
                    self.add_agent(item)
                    print(f"Agent {item} created for directory {item_path}")
                    
    def create_directory(self, path: str):
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Verzeichnis erstellt: {path}")

    def create_directories(self):
        self.create_directory(self.lumidora_dir)
        self.create_directory(self.agent_dir)

    def add_agent(self, agent_name: str):
        # Überprüfen, ob der Agent bereits existiert, um Duplikate zu vermeiden
        if not any(agent.name == agent_name for agent in self.agents):
            new_agent = LumidoraAgent(agent_name, self.agent_dir)
            self.agents.append(new_agent)
            print(f"Agent {agent_name} hinzugefügt und Verzeichnis erstellt.")
        else:
            print(f"Agent {agent_name} existiert bereits und wurde nicht hinzugefügt.")

    def remove_agent(self, agent_name: str):
        self.agents = [agent for agent in self.agents if agent.name != agent_name]
        agent_path = os.path.join(self.agent_dir, agent_name)
        if os.path.exists(agent_path):
            shutil.rmtree(agent_path)
            print(f"Agent {agent_name} und sein Verzeichnis entfernt.")

    def get_agent(self, agent_name: str) -> Optional[LumidoraAgent]:
        for agent in self.agents:
            if agent.name == agent_name:
                return agent
        return None

