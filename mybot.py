from telegram import message, parsemode, user
from poll import start
import telegram
from telegram.ext import Updater, Filters
from telegram.ext import MessageHandler, MessageFilter,CommandHandler
import wikipedia as wiki
wiki.set_lang("es")


#identificador del bot
Token="1779155446:AAFu36Ef9BFP2mWX1Y_9qc9nA_nZfqh0_Us"



#Info del bot
def getBotinfo(update,context):
    bot=context.bot
    id=update.message.chat_id
    username= update.effective_user["first_name"]
    print(f'El usuario {username} ha solicitado información')
    bot.sendMessage(
        chat_id= id,
        parse_mode= "HTML",
        text="""Hola, soy un BOT bot de prueba &#128517 ;Mis comandos por el momento son:
        <code>wiki (palabra a buscar)</code>"""
    )

#Funcion para el buscador en wikipedia
# def searchWord(update, context):
#     bot = context.bot
#     updateMsg = getattr(update,"message", None)
#     chatID = update.message.chat_id
#     text = update.message.text #obtener el mensaje que envio el usuario por el chat
    
#     if text.startswith("wiki "):
#         word = text.replace("wiki ","")
#         bot.sendMessage(
#             chat_id=chatID,
#             text= f"{wiki.summary(word)}\n {wiki.page(word).url}"
#        )
#     bot.sendMessage(
#         chat_id =chatID,
#         text=text
#     )
#     print(text)

#Start command
def start(update,context):
    bot = context.bot
    username = update.effective_user["first_name"]
    update.message.reply_text(f'Hola sr(a)  {username}, ¿En qué le puedo ayudar?, por favor escriba /Bot_info')


def welcomeMsg(update, context):
    bot = context.bot
    chatID = update.message.chat_id
    updateMsg = getattr(update,"message",None)
    for user in updateMsg.new_chat_members:
        userName= user.first_name
    print(f"el usuario {userName} ha ingresado al grupo" )

    bot.sendMessage(
        chat_id = chatID,
        parse_mode = "HTML",
        text = """Hola {}, <a href="https://i.pinimg.com/originals/41/4a/fb/414afbe8b5b99632259de74d5060fb7e.gif">Bienvenid@</a> al grupo
        """.format(userName)
    )


def deleteMsg(bot, chatID,messageID, userName):
    try:
        bot.delete_message(chatID,messageID)
        print(f"El mensaje de {userName} se elimino su mensaje por malas palabras")
    except Exception as e:
        print(e)

def echo(update, context):
    bot = context.bot
    updateMsg = getattr(update,"message", None)
    messageID = updateMsg.message_id #obtener id del mensaje
    chatID = update.message.chat_id
    username = update.effective_user["first_name"]
    text = update.message.text #obtener el mensaje que envio el usuario por el chat

    print(f" el usuario {username} ha enviado un mensaje al grupo")

    badWord = "pta"

    if badWord in text:
        deleteMsg(bot,chatID,messageID,username)
        bot.sendMessage(
            chat_id=chatID,
            text="Se eliminó el mensaje por mal hablad@"
        )
        
    if text.startswith("wiki "):
        word = text.replace("wiki ","")
        bot.sendMessage(
            chat_id=chatID,
            text= f"{wiki.summary(word)}\n {wiki.page(word).url}"
       )
        



#Crear el bot
if __name__ == "__main__":
    mybot= telegram.Bot(Token)
    print(mybot.get_me())

#Conecta y recibe mensajes
updater = Updater(mybot.token, use_context=True)

#crea el dispacher
dp=updater.dispatcher

#Creamos los recibimietos de mensajes
dp.add_handler(CommandHandler("Bot_info",getBotinfo))
dp.add_handler(CommandHandler("Start", start))
dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcomeMsg))
dp.add_handler(MessageHandler(Filters.text, echo))
# dp.add_handler(MessageHandler(Filters.text, searchWord))

#mantenemos activo el bot
updater.start_polling() #mensajes entrantes
updater.idle() #poder terminar el bot con Ctrl+c

#print(searchWord("Python", "")+"\n"+wiki.page("Python").url)

