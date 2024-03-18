from setuptools import find_packages, setup


setup(
    name = 'Medical_Chatbot',
    version= '0.0.1',
    author= 'ajit',
    author_email= 'ajitkumar121996@gmail.com',
    packages= find_packages(),
    install_requires = ["openai","langchain","huggingface","ctransformers","sentence-transformers==2.2.2","pinecone-client","flask","pypdf","python-dotenv","langchain-community"]

)