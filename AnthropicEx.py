# Anthropic is an American artificial intelligence (AI) startup and public-benefit corporation, 
# founded by former members of OpenAI. Anthropic specializes in developing general AI systems and 
# language models, with a company ethos of responsible AI usage. Anthropic develops a chatbot, 
# named Claude. Similar to ChatGPT, Claude uses a messaging interface where users can submit questions or 
#requests and receive highly detailed and relevant responses.

from langchain.chat_models import ChatAnthropic
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,    
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = ChatAnthropic()

messages = [
    HumanMessage(content="Translate this sentence from English to French. I love programming.")
]

chat(messages)
