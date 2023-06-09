from langchain.chat_models import ChatVertexAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    HumanMessage,
    SystemMessage
)

chat = ChatVertexAI()

messages  = [
    SystemMessage(content="You are a helpful assistant the translates English to French."),
    HumanMessage(content="Translate this sentance from English to French. I love programming.")
]
chat(messages)


template="You are a helpful assistant that translates (input_language) to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

#get a chat completion from the formatted message
chat(chat_prompt.format(input_language="English", output_language="French", text="I love progamming.").to_message())

