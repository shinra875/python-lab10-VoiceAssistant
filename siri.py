import json, pyaudio,requests, pyttsx3
from vosk import Model, KaldiRecognizer

engine = pyttsx3.init()

model = Model('small_model')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


# функция прослушивания юзера 
def listen():
    while True:
        data = stream.read(4000,exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']

# массивы всех произнесенных слов и всех математических фактов соответственно
text_mass = ['pass']
all_math_facts = ['pass']


for text in listen():
    
    # команда приветсвтия
    if text == 'привет':
        print('\n', 'и тебе привет))')
        engine.say("и тебе привет))")
        engine.runAndWait()
        text_mass.append(text)
        
        
    # команда факта 
    elif text == 'сири':
        if text != text_mass[-1] and len(text_mass)!=0:
            # вывод рандомного факта из математики
            response = requests.get('http://numbersapi.com/random/math')
            math_fact = response.text
            print('\n',math_fact)
            engine.say(math_fact)
            engine.runAndWait()
            text_mass.append(text)
            all_math_facts.append(math_fact)
        else:
            print('\n',all_math_facts[-1])
            engine.say('Вы снова просите факт (ту же команду), хм, хорошо, вот он!')
            engine.runAndWait()        
        
        
    # команда нового факта
    elif text == 'ещё':
        # вывод рандомного факта из математики
        response = requests.get('http://numbersapi.com/random/math')
        math_fact = response.text
        print('\n',math_fact)
        engine.say(math_fact)
        engine.runAndWait()
        text_mass.append(text)
        all_math_facts.append(math_fact)
        
        
    # команда предыдущего факта
    elif text == 'назад':  # не поддерживает перескока на несколько назад. можно только предыдущий
        print('\n', all_math_facts[-2])
        engine.say(all_math_facts[-2])
        engine.runAndWait()
        
        
    # команда всех фактов
    elif text == 'все':
        print('\n', all_math_facts[1:])
        engine.say('хочешь все факты? ну на')
        engine.runAndWait()
        
        
    # команда всех произнесенных слов
    elif text == 'слова':
        print('\n', text_mass[1:])
        engine.say('тебе все слова повторить? мне не жалко')
        engine.runAndWait()
        
        
    # команда прощания
    elif text == 'пока':
        print('\n','блин, ну ладно(')
        engine.say("блин, ну ладно(")
        engine.runAndWait()
        text_mass.append(text)
        quit()
        
        
    else:
        print('\n',text)
        engine.say(text)
        engine.runAndWait()
        text_mass.append(text)
