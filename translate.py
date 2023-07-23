from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

if __name__ == "__main__":
    print("Welcome to the Translator App!")
    while True:
        input_text = input("Enter the text you want to translate (or 'q' to quit): ")
        
        if input_text.lower() == 'q':
            print("Goodbye!")
            break
        
        target_language = input("Enter the target language (e.g., 'es' for Spanish, 'fr' for French): ")
        
        try:
            translated_text = translate_text(input_text, target_language)
            print(f"Translated text: {translated_text}\n")
        except Exception as e:
            print("Error occurred:", e)