import wikipedia 
import datetime
import webbrowser
import os
import sys
import  nancy as n
import search_net as s
import speech as sp

def Wish_Me():
    
    hour = int(datetime.datetime.now().hour)
    if hour >0 and hour <12:
        n.speak('Good Morning,sir!')
    elif hour >=12 and hour <18:
        n.speak('Good afternoon,sir!')
    else:
        n.speak('good evening,sir!')
    n.speak('how can i help you')
    

def youtube():
    n.speak('wait ,opening youtube')
    webbrowser.open_new('youtube.com')
     
     
def google():
    n.speak('wait ,opening google')
    webbrowser.open_new('google.com')
     
    
def music(): 
    n.speak('wait ,playing music')
    music_dir = 'E:\\music\\atif aslam'
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir,songs[0]))
    
def videoseries():
    n.speak('wait  opening video series')
    n.speak('which episode you want to play')
    query = sp.Take_Command()
    system = 'E:\Jack Ryan'
    video = os.listdir(system)
    if 'first' in query:
        os.startfile(os.path.join(system,video[0]))
        
    elif 'second' in query:
        os.startfile(os.path.join(system,video[1]))
   
    

def msword():
    n.speak('wait ,opening ms word')
    music_dir = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office'
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir,songs[10]))
    
   

def msexcel():
    n.speak('wait ,opening ms excel')
    music_dir = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office'
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir,songs[1]))
    
    
def chrome():
    n.speak('wait  open chrome')
    _dir = 'C:\Program Files (x86)\Google\Chrome\Application'
    chrom = os.listdir(_dir)
    os.startfile(os.path.join(_dir,chrom[3]))
'''  n.speak('what you want to search sir')
    query=n.Take_Command()
    
    new = 2
   # taburl='http://google.com/?#q='
    webbrowser.open(_dir+query,new=new)
'''
def search():  
    n.speak('what you want to search')
    q =sp.Take_Command()
    s.get_results(q)
        
    
          
def time():
     strTime = datetime.datetime.now().strftime('%H:%M:%S')
     n.speak(f'the time is {strTime}')
     
            
def reminders(rem):
    n.speak('hello sir today  your reminder is '+ rem)
     
     
def nancy():
    hour = int(datetime.datetime.now().hour)
    if hour >0 and hour<=19:
        
        n.speak('bye ,have a good day')
        sys.exit('bye ,have a good day')
    else:
         n.speak('good night sir')
         sys.exit('good night sir')
         
def wiki(query):
    n.speak('wait ')
    n.speak('searching wikipedia...')
    results = wikipedia.summary(query,sentences=2)
    n.speak('according to wikipedia')
    print(results)
    n.speak(results)
     
     
def nancy_f(a):
    if 'hey nancy' in a:
        n.speak('yes ')
        
        
    elif  'good morning 'or 'good afternoon '  in a:
        Wish_Me()
        
    elif 'hi nancy' or 'helo nancy' in a:
        n.speak('helo sir')
        
    elif 'great nancy' in a :
        n.speak('thaks sir')
        
        
        
def sleep():
    n.speak('wait sir sleep your computer')
    shortcut_dir = 'D:\shortcut'
    _dir = os.listdir(shortcut_dir)
    os.startfile(os.path.join(shortcut_dir,_dir[4]))
           
def shutdown():
    n.speak('wait sir shutdowning your computer')
    shortcut_dir = 'D:\shortcut'
    _dir = os.listdir(shortcut_dir)
    os.startfile(os.path.join(shortcut_dir,_dir[3]))
    

def restart():
    n.speak('wait sir restarting your computer')
    shortcut_dir = 'D:\shortcut'
    _dir = os.listdir(shortcut_dir)
    os.startfile(os.path.join(shortcut_dir,_dir[2]))
    
    

   
def keyboard():
    n.speak('wait sir start keyboard')
    shortcut_dir = 'D:\shortcut'
    _dir = os.listdir(shortcut_dir)
    os.startfile(os.path.join(shortcut_dir,_dir[1]))
   
    
 
def calculator():
    n.speak('wait sir opening calculator')
    shortcut_dir = 'D:\shortcut'
    _dir = os.listdir(shortcut_dir)
    os.startfile(os.path.join(shortcut_dir,_dir[0]))
 





