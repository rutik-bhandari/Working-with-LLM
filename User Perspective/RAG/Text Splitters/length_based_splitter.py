from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('User Perspective\\RAG\\Document Loaders\\dl-curriculum.pdf')

docs = loader.load()

ipl = '''
Indian Premier League (IPL)

The Indian Premier League (IPL) is one of the world's most popular T20 cricket leagues. It was started in 2008 by the BCCI and features franchise teams representing different Indian cities.

IPL matches are played in the fast-paced Twenty20 format, where each team gets 20 overs to score runs. The tournament brings together some of the best Indian and international cricketers, making it highly competitive and entertaining.

Apart from cricket, the IPL has become a major sporting and business event, attracting millions of fans, sponsors, and viewers every year. It has also provided a platform for young Indian players to showcase their talent and play alongside international stars.

In short, IPL combines cricket, entertainment, and global sporting talent in one of the biggest T20 tournaments in the world.
'''
splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

# result = splitter.split_text(ipl)  

result = splitter.split_documents(ipl)  

print(result)