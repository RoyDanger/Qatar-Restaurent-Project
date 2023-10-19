from docx import Document
import openai
import pandas as pd

# Set OpenAI API key
api_key = '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'  # Replace with your API key
openai.api_key = api_key

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)

def translate_text(input_text):
    # Split the input text into smaller chunks
    chunk_size = 1000  # Maximum characters per chunk
    chunks = [input_text[i:i + chunk_size] for i in range(0, len(input_text), chunk_size)]

    # Translate each chunk to English
    translated_chunks = []
    for chunk in chunks:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Translate the following Japanese text to English: '{chunk}'",
            max_tokens=200  # Adjust token limit as needed; initially 50
        )
        translated_chunks.append(response.choices[0].text)

    # Combine the translated chunks into a single translated text
    translated_text = ' '.join(translated_chunks)

    return translated_text

def translate_file(file_path):
    # Determine the file type and process accordingly
    if file_path.endswith(".docx"):
        input_text = extract_text_from_docx(file_path)
    elif file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
        # Combine all text columns into a single string
        input_text = " ".join(df.select_dtypes(include=['object']).stack().tolist())
    else:
        print("Unsupported file format")
        return

    # Translate the text
    translated_text = translate_text(input_text)

    return translated_text

# Ask the user for the file path
file_path = input("Enter the path to the document (e.g., /path/to/document.docx or /path/to/data.csv): ")

# Translate the file
translated_text = translate_file(file_path)
print(translated_text)
