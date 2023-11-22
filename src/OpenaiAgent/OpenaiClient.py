from openai import OpenAI
from .LangchainMemoryAgent import LangChainMemoryAgent
import json

class OpenaiClientConfigLoader:
    """Load OpenAI client config from a json file"""
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config = None
        self.load_config()
    
    def load_config(self):
        """Load config from file"""
        with open(self.config_file_path, "r") as f:
            self.config = json.load(f)
    
    def get_config(self):
        """Return config"""
        return self.config
    
class LangchainClient:
    """Client for Langchain"""
    def __init__(self, config_file_path):
        self.config = OpenaiClientConfigLoader(config_file_path).get_config()
        self.api_key = self.config["api_key"]
        self.client = LangChainMemoryAgent(openai_api=self.api_key,
                                           system_prompt="You are an assistant in a discord server. You can reply anything you want. You are just one of them.\
                                            Do not contain any sentence which reminds us of your answer may incorrect to reduce answer length. \
                                            Because we already know you are an language model.",
                                           )
    
    def chat(self, input):
        """Chat with Langchain"""
        return self.client.chat(message=input)
    
    def clear_memory(self):
        """Clear memory"""
        self.client.clear_memory()

class OpenaiClient:
    def __init__(self, config_file_path):
        self.config = OpenaiClientConfigLoader(config_file_path).get_config()
        self.api_key = self.config["api_key"]
        self.client = OpenAI(api_key=self.api_key)

    def chat(self, messages):
        response = self.client.chat.completions.create(
            model=self.config["gpt_model"],
            messages=messages
        )
        return response.choices[0].message.content
    
    def tts(self, text):
        speech_file_path = "speech.mp3"
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )
        response.stream_to_file(speech_file_path)
        return speech_file_path