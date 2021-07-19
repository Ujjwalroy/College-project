from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import sys
import  conversation
import nancy as n
import speech as s

bot = ChatBot(
    'nancy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
)
trainer = ListTrainer(bot)

trainer.train(conversation.conversation())

# The following loop will execute each time the user enters input
while True:
        
        
    try:
        bot_input = s.Take_Command()
            
        if 'bye' in bot_input:
            sys.exit()
            
        else:
            bot_input = bot.get_response(bot_input)
            print('nancy: ',bot_input)
            n.speak(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
