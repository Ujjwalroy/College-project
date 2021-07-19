import speech_recognition as sr

def Take_Command():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('you said : {}',format(text))

    except:
        print('sorry could not recognize your voice')
      

Take_Command()
