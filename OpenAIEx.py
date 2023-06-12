import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

load_dotenv()
os.environ["OPENAI_API_KEY"] = "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"

chat = ChatOpenAI(temperature=0)

messages = [
    SystemMessage(content="You are a helpful assistent that translates English to French."),
    HumanMessage(content="Translate this sentence from English to French. I love proramming.")
]
chat(messages)

template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

#get a chat completion from a formatted messages
result = chat(chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages())
print(result)