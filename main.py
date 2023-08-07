from env import SL_CHAT, PCT_CHAT, CLUSTER_CHAT, TOKEN
import requests, emoji
import telebot

bot = telebot.TeleBot(TOKEN)
GROUP_CHATS = [SL_CHAT, CLUSTER_CHAT, PCT_CHAT]

@bot.message_handler(commands=['start', 'help'])
def say_hello(message):
    if message != SL_CHAT and message.chat.id in GROUP_CHATS: return
    bot.reply_to(message, '\n'.join([
        'Hi, I am the lovely PCT 5 KIRISUS Telegram Bot! How can I help you for today?',
        '',
        'Here are some commands that you can try:',
        '/start or /help to display this message again',
        '/calendar to obtain the latest activities in PH',
        '/iglinks to get all the links to the interest groups',
        '/map for a nicely updated map of PGP',
        '/mahjong if you need a mahjong friend from the PCT chat so bad ;)',
        '/pinned to check all the important pinned messages on the PCT chat!'
    ]))

@bot.message_handler(commands=['calendar'])
def calendar(message):
    if message.chat.id in GROUP_CHATS: return
    bot.reply_to(message, 'Sending the PH calendar in a bit!')
    bot.send_document(message.chat.id, open('assets/PH Calendar AY23-24.pdf', 'rb'))

@bot.message_handler(commands=['iglinks'])
def iglinks(message):
    if message.chat.id in GROUP_CHATS: return
    bot.reply_to(message, 'Do check here!\nhttps://t.me/nuspioneer/1137')

@bot.message_handler(commands=['map'])
def pgpmap(message):
    if message.chat.id in GROUP_CHATS: return
    bot.reply_to(message, 'Sending the PGP map in a bit!')
    bot.send_document(message.chat.id, open('assets/PGP Map.jpg', 'rb'))

@bot.message_handler(commands=['mahjong'])
def mahjong(message):
    if message.chat.id in GROUP_CHATS: return
    bot.reply_to(message, 'Sending the Mahjong gamebook and the jio in a bit!')
    bot.send_document(message.chat.id, open('assets/SG Mahjong Rules.pdf', 'rb'))
    send_message(PCT_CHAT, f"@{message.chat.username} wants to play mahjong 🀄️🀄️, react to this message if you're in!")

@bot.message_handler(commands=['remindmrp'])
def remindmrp(message):
    if message.chat.id != SL_CHAT: return
    bot.reply_to(message, 'Hi all PMs! Reminder that MRP and dashboard are due soon so please make sure you submit them on time 💅💅💅')

from env import *
@bot.message_handler(commands=['pinned'])
def pinned(message):
    if message.chat.id in GROUP_CHATS and message.chat.username != RUSSELL: return # :)
    bot.reply_to(message, PINNED)

def send_message(chat_id, message):
    r = requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage", params={
        "chat_id": chat_id,
        "parse_mode": "Markdown",
        "text": emoji.emojize(message),
        "disable_web_page_preview": True,
    })

if __name__ == '__main__':
    bot.infinity_polling()