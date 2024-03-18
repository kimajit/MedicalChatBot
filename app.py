from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
# from langchain.vectorstores import Pinecone
import pinecone
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')
embeddings = download_hugging_face_embeddings()


# pinecone.init(api_key=PINECONE_API_KEY,
#               environment=PINECONE_API_ENV)

index_name="medicalchatbot"

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

chain_type_kwargs={"prompt": PROMPT}
docsearch=PineconeVectorStore.from_existing_index(index_name, embeddings)
model_path ="/Users/ajit/.cache/huggingface/hub/models--TheBloke--Llama-2-13B-chat-GGML/snapshots/3140827b4dfcb6b562cd87ee3d7f07109b014dd0/llama-2-13b-chat.ggmlv3.q5_1.bin"

llm=CTransformers(model=model_path,
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.8})


qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)



@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)