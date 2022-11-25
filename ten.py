from telegram import Update
from telegram.ext import MessageHandler,  Updater
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.filters import Filters
from final import *

def predict(user_input:str)->str:
    res='hello'
    intents = Pclass(user_input, newWords, ourClasses)
    res = getRes(intents, ourData)
    #res=final.ourResult(user_input)
    return res


def MessageRespond(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    print(f'{user_input=}')
    reply = predict(user_input)
    
    
    update.message.reply_text(f'{reply}')


app = Updater("5935900154:AAGnNJVjYBt3_Sa4E0hTpARE-YOiMvZpJi4",use_context=True)

app.dispatcher.add_handler(MessageHandler(Filters.text, MessageRespond))

print("App Starting..")
app.start_polling()
