from googletrans import Translator
translator = Translator()
hindi_text = 'नमस्ते दोस्तों'
english_text = translator.translate(hindi_text, src='hi', dest='en').text
print(english_text)