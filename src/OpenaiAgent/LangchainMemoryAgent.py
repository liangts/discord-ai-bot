from operator import itemgetter

from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough

class LangChainMemoryAgent:
    def __init__(self, openai_api,
                 system_prompt:str,
                 model: str = "gpt-4-1106-preview",
                 memory_limit: int = 8):
        self.model = model
        self.memory_limit = memory_limit
        self.memory = ConversationBufferMemory(return_messages=True)
        self.memory.load_memory_variables({})

        self.llm = ChatOpenAI(api_key=openai_api, model=model)
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{input}"),
            ]
        )
        self.chain = (
            RunnablePassthrough.assign(history=RunnableLambda(self.memory.load_memory_variables)
                                       | itemgetter("history"))
            | self.prompt
            | self.llm
        )

    def chat(self, message: str) -> str:
        response = self.chain.invoke({"input": message})
        self.memory.save_context({"input": message}, {"output": response.content})
        return response.content
    
    def clear_memory(self):
        self.memory.clear()