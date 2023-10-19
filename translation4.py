from docx import Document
import openai

# Set OpenAI API key
api_key = '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'  # Replace with your API key
openai.api_key = api_key

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)

def split_text_into_chunks(text, chunk_size=1000):
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

def translate_long_text(input_text):
    translated_chunks = []

    # Split the input_text into smaller chunks (sentences, paragraphs, etc.)
    # You can customize the chunk size based on your needs
    chunk_size = 1000  # Maximum characters per chunk
    chunks = [input_text[i:i + chunk_size] for i in range(0, len(input_text), chunk_size)]

    # Translate each chunk to English
    for chunk in chunks:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Translate the following Japanese text to English: '{chunk}'",
            max_tokens=50  # Adjust token limit as needed
        )
        translated_chunks.append(response.choices[0].text)

    # Combine the translated chunks into a single translated text
    translated_text = ' '.join(translated_chunks)

    return translated_text

# Function to translate a Word document
def translate_word_document(docx_file):
    # Extract text from Word document
    input_text = extract_text_from_docx(docx_file)

    # Split the text into chunks
    chunks = split_text_into_chunks(input_text)

    # Translate and store each chunk
    translated_chunks = []
    for chunk in chunks:
        translated_chunk = translate_long_text(chunk)
        translated_chunks.append(translated_chunk)

    # Combine translated chunks into the translated document
    translated_document = '\n'.join(translated_chunks)

    return translated_document

# Example usage:
translated_document = translate_word_document("/Users/profielddev/Desktop/py4e/jatext.docx")
print(translated_document)