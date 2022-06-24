from rubpy import Bot,Uploader
from  threading import Thread
from random import randint
import time
def get_logo(up,chat,text,):
	true=False
	while (true!=True):
		time.sleep(00.1)
		try:
			up.sendPhoto(chat['object_guid'], "http://api.hajiapi.tk/ephoto360?type=text&id="+str(randint(1,138))+"&text="+text[5:] , caption=('꙰꙰꙰꙰꙰꙰꙰𝑻𝒉𝒆 𝒍𝒐𝒈𝒐 𝒚𝒐𝒖 𝒘𝒂𝒏𝒕 𝒘𝒂𝒔 𝒄𝒓𝒆𝒂𝒕𝒆𝒅 ꙰\n\nヅᴾˡᵉᵃˢᵉ ˢᵘᵇˢᶜʳⁱᵇᵉ ᵗᵒ ᵒᵘʳ ᶜʰᵃⁿⁿᵉˡ₪\n\n𖤍 @logomakersupport ʝօɨռ'), message_id=chat['last_message']['message_id'])
			true=True
		except:
			true=False

auth = ("boqnemcsubvqzlecdevwqqjfjurwkoym")
bot = Bot(auth, displayWelcome=False)
up=Uploader(auth)
guid = ("u0CrOci0542b2372d5a201dc7c846788")

list_message_seened = []

def indo():
    while 1:
        try:
            chats:list = bot.getChatsUpdate()
            if chats!=[]:
                for chat in chats:
                    m_id = chat['object_guid'] + chat['last_message']['message_id']
                    if not m_id in list_message_seened:
                        access = chat['access']
                        if chat['abs_object']['type'] == 'User' and chat["object_guid"]!=guid:
                            text:str = chat['last_message']['text']
                            if 'SendMessages' in access and chat['last_message']['type'] == 'Text' and text.strip() != '':
                                text = text.strip()
                                if text.startswith("logo "):
                                    Thread(target=get_logo,args=(up,chat,text,)).start()
                                list_message_seened.append(m_id)
        
        except Exception as e:
            print(e)
            pass
            
indo()