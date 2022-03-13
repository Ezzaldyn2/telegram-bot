import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def boten(message):
	
    
    
    mas = types.InlineKeyboardMarkup(row_width=2)
    
    A = types.InlineKeyboardButton(text ="USER (BFFFL)", callback_data="F1")
    
    E = types.InlineKeyboardButton(text ="USER (BFFF2)", callback_data="F2")
    
    M = types.InlineKeyboardButton('丕賱賲胤賵乇', url='https://t.me/SidraTools')
    
    mas.add(A,E,M)
    
    bot.send_message(message.chat.id, f"- 兀賴賱丕賸 亘賰賸  !\n\n- 亘賵鬲 鬲卮賰賷乇 賷賵夭乇丕鬲 鬲賱噩乇丕賲 馃鈥嶐煉籠n\n鈾伙笍 賱賵丨丞 丕賱鬲丨賰賲 丕賱禺丕氐賴 亘賰 鈾笍",reply_markup=mas)
    
    
@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	
	
	global nam
	
	if call.data =="SidraTools":
		
		mas = types.InlineKeyboardMarkup(row_width=2)
		
		A = types.InlineKeyboardButton(text ="USER (BFFFL)", callback_data="F1")

		E = types.InlineKeyboardButton(text ="USER (BFFF2)", callback_data="F2")
		
		M = types.InlineKeyboardButton('丕賱賲胤賵乇', url='https://t.me/SidraTools')
		
		M = types.InlineKeyboardButton('丕賱賲胤賵乇', url='https://t.me/SidraTools')
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- 兀賴賱丕賸 亘賰賸 毓夭賷夭賷 丕賱賲爻鬲禺丿賲 \n\n- 亘賵鬲 鬲卮賰賷乇 賷賵夭乇丕鬲 鬲賱噩乇丕賲 馃鈥嶐煉籠n\n鈾伙笍 賱賵丨丞 丕賱鬲丨賰賲 丕賱禺丕氐賴 亘賰 鈾笍",reply_markup=mas)

	elif call.data =="F1":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			username = str(us)+str(un)+str(un)+str(un)+str(ua)
			url = "https://t.me/"+str(username)
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"鈥� 岽溠曖磭蕗纱岽�岽嶀磭 岽涐磭薀岽嚿⑹�岽�岽�  鉁揬n鈹�鈹�鈹�鈹�鈹�鈹� 鈥� 鉁р湩 鈥� 鈹�鈹�鈹�鈹�鈹�鈹�\n鈥� 岽溠曖磭蕗纱岽�岽嶀磭 : @{username}\n鈹�鈹�鈹�鈹�鈹�鈹� 鈥� 鉁р湩 鈥� 鈹�鈹�鈹�鈹�鈹�鈹�\n鈥� @SidraTools")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('丕賱賲胤賵乇', url='https://t.me/SidraTools')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
				
			
		
		
	elif call.data =="F2":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xm = "0987654321"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			bs = str(''.join(random.choice(xm)for i in range(1))) 
			username = str(us)+str(un)+str(un)+str(un)+str(bs)
			url = "https://t.me/"+str(username)
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"鈥� 岽溠曖磭蕗纱岽�岽嶀磭 岽涐磭薀岽嚿⑹�岽�岽�  鉁揬n鈹�鈹�鈹�鈹�鈹�鈹� 鈥� 鉁р湩 鈥� 鈹�鈹�鈹�鈹�鈹�鈹�\n鈥� 岽溠曖磭蕗纱岽�岽嶀磭 : @{username}\n鈹�鈹�鈹�鈹�鈹�鈹� 鈥� 鉁р湩 鈥� 鈹�鈹�鈹�鈹�鈹�鈹�\n鈥� @SidraTools")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}', callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('丕賱賲胤賵乇', url='https://t.me/SidraTools')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://appointm3ent.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
