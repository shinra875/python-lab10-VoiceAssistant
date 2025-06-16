# def recAndPlay():
#    # этот блок кода слушает и воспроизводит записанную речь
#     import pyaudio
#     import wave  # хз зачем, ни на что не влияет

#     FORMAT = pyaudio.paInt16  # Формат звука (16 бит, стерео)
#     CHANNELS = 2
#     RATE = 44100  # Частота дискретизации
#     CHUNK = 1024  # Размер блока данных

#     p = pyaudio.PyAudio()



#     # Запись звука
#     stream = p.open(format=FORMAT,
#                     channels=CHANNELS,
#                     rate=RATE,
#                     input=True,
#                     frames_per_buffer=CHUNK)

#     frames = []

#     for i in range(0, int(RATE / CHUNK * 5)):
#         data = stream.read(CHUNK)
#         frames.append(data)

#     # Остановка записи
#     stream.stop_stream()
#     stream.close()




#     # Воспроизведение записанного звука
#     stream = p.open(format=FORMAT,
#                     channels=CHANNELS,
#                     rate=RATE,
#                     output=True)

#     for frame in frames:
#         stream.write(frame)

#     # Остановка воспроизведения
#     stream.stop_stream()
#     stream.close()

#     p.terminate()

# def tts_voice_stats():
#     # # Для произношения текста голосом и настройки характеристик голоса

#     # этот блок произносит данный ему текст
#     import pyttsx3
#     engine = pyttsx3.init()
#     engine.say("я@ты@я@ты@я@ты@я@ты@я@ты@")
#     engine.runAndWait()

#     text = 'какой-нибудь текст'
#     tts = pyttsx3.init()  # создание объекта
#     rate = tts.getProperty('rate') #Скорость произношения
#     tts.setProperty('rate', rate-40)  # установление скорости произношения  

#     volume = tts.getProperty('volume') #Громкость голоса
#     tts.setProperty('volume', volume+0.9)  # установление громкости [0;1]

#     voices = tts.getProperty('voices')

#     # Задать голос по умолчанию
#     tts.setProperty('voice', 'ru') 

#     # Попробовать установить предпочтительный голос
#     for voice in voices:
#         if voice.name == 'Anna':
#             tts.setProperty('voice', voice.id)

#     tts.say(text)
#     tts.runAndWait()


#     # import pyttsx3
#     # engine = pyttsx3.init() # object creation

#     # """ RATE - скорость"""
#     # rate = engine.getProperty('rate')   # getting details of current speaking rate
#     # # print (rate)                        #printing current voice rate
#     # engine.setProperty('rate', 125)     # setting up new voice rate


#     # """VOLUME - громкость [0;1]"""
#     # volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#     # # print (volume)                          #printing current volume level
#     # engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1

#     # """VOICE - голос (рус/англ версия голоса (не влияет на м/ж))"""
#     # voices = engine.getProperty('voices')       #getting details of current voice
#     # #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#     # engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


#     # # он не произносит несколько команд, весь его текст нужно умещать в одну функцию

#     # # engine.say("big brown fox is jumping over the tree")
#     # engine.say('My current speaking rate is ' + str(rate))

#     # engine.runAndWait()
#     # engine.stop()


#     # # если этот блок оставить, то все будет работать, но будет вызывать ошибку в терминале в конце

#     # # """Saving Voice to a file"""
#     # # # On linux make sure that 'espeak' and 'ffmpeg' are installed
#     # # engine.save_to_file('Hello World', 'test.mp3')
#     # # engine.runAndWait()


# import requests
# import pyttsx3


# # вывод рандомного факта из математики
# response = requests.get('http://numbersapi.com/random/math')
# math_fact = response.text
# print(math_fact)

# engine = pyttsx3.init()

# """VOICE - голос (рус/англ версия голоса (не влияет на м/ж))"""
# voices = engine.getProperty('voices')       #getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male (фулл на английском)
# # engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female (русские числа + ломанный английский)
# engine.say(math_fact)  # озвучка текста
# engine.runAndWait()  # запуск и ожидание..? хз


# этот блок кода слушает, записывает в файл (и воспроизводит) записанную речь








# import wave
# import sys

# import pyaudio

# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 1 if sys.platform == 'darwin' else 2
# RATE = 44100
# RECORD_SECONDS = 5

# with wave.open('output.wav', 'wb') as wf:
#     p = pyaudio.PyAudio()
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)

#     stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

#     print('Recording...')
#     for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
#         wf.writeframes(stream.read(CHUNK))
#     print('Done')

#     stream.close()
#     p.terminate()




# import vosk
# import sys
# import os
# import wave
# import json

# # Загрузка модели
# if not os.path.exists("model"):
#     print("Пожалуйста, скачайте модель с https://alphacephei.com/vosk/models и распакуйте ее в текущий каталог.")
#     sys.exit()

# model = vosk.Model("model")

# # Открытие аудиофайла
# wf = wave.open('output.wav', "rb")
# rec = vosk.KaldiRecognizer(model, wf.getframerate())

# # Распознавание речи
# while True:
#     data = wf.readframes(4000)
#     if len(data) == 0:
#         break
#     if rec.AcceptWaveform(data):
#         result = json.loads(rec.Result())
#         print(f"Распознанный текст: {result['text']}")


import json, pyaudio,requests, time, pyttsx3
from vosk import Model, KaldiRecognizer

engine = pyttsx3.init()

model = Model('small_model')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def listen():
    while True:
        data = stream.read(4000,exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']


text_mass = []
all_math_facts = ['pass']

for text in listen():
    if text == 'привет':
        print('\n', 'и тебе привет))')
        engine.say("и тебе привет))")
        engine.runAndWait()
        text_mass.append(text)
        
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
            print(text_mass)
            print(all_math_facts)
        else:
            print('\n',all_math_facts[-1])
            engine.say('Вы снова просите факт (ту же команду), хм, хорошо, вот он!')
            engine.runAndWait()
            
        
        
        
    elif text == 'ещё':
        # вывод рандомного факта из математики
        response = requests.get('http://numbersapi.com/random/math')
        math_fact = response.text
        print('\n',math_fact)
        engine.say(math_fact)
        engine.runAndWait()
        text_mass.append(text)
        all_math_facts.append(math_fact)
        print(text_mass)
        print(all_math_facts)
    
    elif text == 'назад':  # не поддерживает перескока на несколько назад. можно только предыдущий
        print('\n', all_math_facts[-2])
        engine.say(all_math_facts[-2])
        engine.runAndWait()

    elif text == 'все':
        print('\n', all_math_facts)
        engine.say('хочешь все факты? ну на')
        engine.runAndWait()

        
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