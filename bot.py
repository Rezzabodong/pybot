import time, datetime
import telepot
from telepot.loop import MessageLoop
now = datetime.datetime.now()
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Received: %s' % command
    if command == '/hi':
        telegram_bot.sendMessage (chat_id, str("Hi! Sasmitoh Ganteng"))
    elif command == '/time':
        telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
    elif command == '/logo':
        telegram_bot.sendPhoto (chat_id, photo = "https://www.raspberrypi.org/app/uploads/2011/10/Raspi-PGB001.png")
    elif command == '/file':
        telegram_bot.sendDocument(chat_id, document=open('/home/sasmitoh/Downloads/bot.py'))
    elif command == '/audio':
        telegram_bot.sendAudio(chat_id, audio=open('/home/sasmitoh/Downloads/sas.mp3'))
telegram_bot = telepot.Bot('masukan token bot anda')
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print 'Up and Running....'
while 1:
    time.sleep(10)
