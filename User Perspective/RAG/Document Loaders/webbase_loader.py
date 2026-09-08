from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.flipkart.com/cmf-nothing-phone-2-pro-5g-black-128-gb/p/itmf32457aeff519'
loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)