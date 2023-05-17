import os, gradio
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from detectron2.config import get_cfg
import nltk

try:
  nltk.data.find('tokenizers/punkt')
except LookupError:
  nltk.download('punkt')

os.environ['OPENAI_API_KEY'] = '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'

cfg = get_cfg()    
cfg.MODEL.DEVICE = 'gpu'

text_folder = 'AsomBarta-NewsLetter'
loaders = [UnstructuredPDFLoader(os.path.join(text_folder, fn)) for fn in os.listdir(text_folder)]

index = VectorstoreIndexCreator().from_loaders(loaders)

description = '''This is an AI conversational agent who you can ask questions to. The ONLY documents it has access to are the Asom Barta newspapers from July 2022 to May 2023. 
So, the bot can only frame its answers based on its worldview attained from the Asom Barta newspapers. If you ask it about anything not pertaining to the content of the 
newspapers, it will simply reply with "I don't know". Enjoy!'''

def chat_response(query):
  return index.query(query)

interface = gradio.Interface(fn=chat_response, inputs="text", outputs="text", title='Asom Barta Q&A Bot', description=description)

interface.launch(server_name="0.0.0.0", server_port=8080, share=True)