from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

BASE_URL = "https://${TODO}.openai.azure.com"
API_KEY = "..."
DEPLYMENT_NAME = "chat"

model = AzureChatOpenAI(
    openai_api_base = BASE_URL,
    openai_api_version = "2023-03-15-preview",
    deployment_name = DEPLYMENT_NAME,
    openai_api_key = API_KEY,
    openai_api_type = "azure",
)

moedl([HumanMessage(content="Translate this sentence from English to French. I love programming.")])