import pandas as pd
import openai

# Set OpenAI API key
api_key = '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'  # Replace with actual API key
openai.api_key = api_key

# Function to translate text from Japanese to English using GPT-3
def translate_with_gpt3(input_text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following Japanese text to English: '{input_text}'",
        max_tokens=50  # Adjust the token limit as needed
    )
    return response.choices[0].text

# Input text (Japanese text to be translated)
input_text = """
これは日本語のテキストの例で、英語に翻訳されます。
It can be a single sentence or multiple paragraphs.
"""

# Call the function to translate the text
translated_text = translate_with_gpt3(input_text)
print(translated_text)
