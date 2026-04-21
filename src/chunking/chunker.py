from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_text_splitter():
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        separators=[
            "\n\n", # paragraph
            "\n",   # line
            ". ",   # sentence
            " "    # fallback
        ]
    )
    return splitter

def is_valid_chunk(text):
    text = text.strip().lower()
    
    # Skip very small chunks
    if len(text) < 100:
        return False
    
    # Skip table of contents
    if "table of contents" in text:
        return False
    
    # Skip manualslib/navigation junk
    if "manualslib" in text:
        return False
    
    # Skip chunks with mostly headings (all caps lines)
    lines = text.split("\n")
    if len(lines) > 5:
        uppercase_lines = sum(1 for line in lines if line.isupper())
        
        if uppercase_lines > len(lines) * 0.9:
            return False
    
    return True

def chunk_documents(documents):
    splitter = create_text_splitter()
    chunks = splitter.split_documents(documents)
    
    # Filter bad chunks
    filtered_chunks = [
        chunk for chunk in chunks
        if is_valid_chunk(chunk.page_content)
    ]
    
    return filtered_chunks