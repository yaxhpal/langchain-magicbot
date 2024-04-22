from langchain.tools.retriever import create_retriever_tool
from langchain_cohere import CohereEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter

from src.msecrets import COHERE_API_KEY

loader = WebBaseLoader("https://www.sms-magic.com/docs/portal/knowledge-base/sms-magic-web-portal-overview/")
docs = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(docs)
embeddings = CohereEmbeddings(cohere_api_key=COHERE_API_KEY)
db = Chroma.from_documents(documents, embeddings)
retriever = db.as_retriever()

# Create Tools
smsmagic_retriever_tool = create_retriever_tool(
    retriever,
    "smsmagic_search",
    "Search for information about SMS-Magic Portal. For any questions about SMS-Magic, you must use this tool!",
)
