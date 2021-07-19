import file as f
import speech_recognition as sr
import pyttsx3
#import  webbrowser
import speech as s

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 120)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    

'''
def Take_Command():
    query = input('you: ')
    return (query)
'''

if __name__ == "__main__":
   # f.Wish_Me()

    while True:
        query=s.Take_Command()
        print(query)
        
        # logic for executing task based on query
        
        if 'wikipedia' in query:
            query = query.replace('wikipedia ','')
            f.wiki(query)
           
        elif 'open youtube' in query:
           f.youtube()
        
        elif 'open google' in query:
           f.google()
            
      
        elif 'play music' in query:
           f.music()
            
        elif ' time'  in query:
           f.time()
           
        elif 'reminder' in query:
            f.reminder()
        
        elif 'bye nancy' in query:
            f.nancy() 
        elif 'hello'in query:
            speak('hello ,how can i help you')
        
        elif 'what is your name' in query:
            speak('i am nancy')
            
#        else 'ok' in query:
#           speak('hmmm')
            
            
        elif 'hello nancy' in query:
            f.nancy_f(query)
            
        elif 'conversation' in query:
            speak('what type of conversation you would like')
            a =s.Take_Command()
            speak('wait sir')
            import bot1 as c
            
      #  elif ' prediction' or 'predict'in query:
       #     from stock import stock
            
            
        elif 'video series' in query:
           f.videoseries()
           
        elif 'ms word' in query:
            f.msword()
            
        elif 'ms excel' in query:
            f.msexcel()
        
        elif 'chrom' in query:
            f.chrome()
            
        elif 'shutdown' in query:
            f.shutdown()
            
        elif 'restart' in query:
            f.restart()
            
        elif 'sleep' in query:
            f.sleep()
            
        elif 'keyboard' in query:
            f.keyboard()
            
        elif 'calculator' in query:
            f.calculator() 
            
        elif 'search' in query:
            f.search()
            
      
        else:
             speak("i can't understand")
            
        
