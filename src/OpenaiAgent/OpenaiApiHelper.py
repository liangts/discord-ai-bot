class MessageWrapper:
    """Wrapper for messages to be used with OpenAI API"""
    def __init__(self):
        self.messages = [
            # {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            # {"role": "user", "content": "Who won the world series in 2020?"}
        ]

    def get_messages(self):
        """Return message to use"""
        return self.messages
    
    def delete_messages(self):
        """Delete all messages"""
        self.messages = []

    def get_and_delete_messages(self):
        """Return all messages and delete them"""
        messages = self.messages
        self.messages = []
        return messages

    def set_system_content(self, content):
        """Set the message system content"""
        msg = self.message_gen("system", content)
        self.messages.append(msg)

    def add_user_content(self, content):
        """Add user content to the message"""
        msg = self.message_gen("user", content)
        self.messages.append(msg)

    def add_assistnat_content(self, content):
        """Add assistant (response) content to the message"""
        msg = self.message_gen("assistant", content)
        self.messages.append(msg)

    # message generator - single json object
    def message_gen(self, role, content):
        return {"role": role, "content": content}