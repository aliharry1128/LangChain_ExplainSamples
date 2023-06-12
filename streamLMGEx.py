import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
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
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

load_dotenv()
os.environ["OPENAI_API_KEY"] = "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."

chat = ChatOpenAI(temperature=0)

print(chat([HumanMessage(lmg content="wallet address: TFEASYZxuJswcp72rjVM5diWfiGE4SG88M  USDT network: Tether(USDT) Trc20"]))
