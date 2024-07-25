from django.shortcuts import render
from deep_translator import GoogleTranslator

# Create your views here.

def translate(request):
    if request.method == 'POST':
        text = request.POST['text']
        lang = request.POST['lang']
        translated_text = handle_translation(text, lang)
        context = {'translated_text': translated_text}
    else:
        context = {}

    return render(request, 'translator/index.html', context)

def handle_translation(text, lang):
    translator = GoogleTranslator(source='auto', target=lang)
    translated_text = translator.translate(text)
    return translated_text