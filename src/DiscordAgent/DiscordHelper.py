import json
class DiscordHelper:
    """Static methods to help with Discord API calls"""

    @staticmethod
    async def send_over_length_message(channel, content):
        """Send a message over 2000 characters by splitting it into multiple messages"""
        while (len(content) > 2000):
            await channel.send(content[:2000])
            content = content[2000:]
        await channel.send(content)

class DiscordClientConfig:
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