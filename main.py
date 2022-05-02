import os
import telebot

bot = telebot.TeleBot("1957971904:AAFNpwDXK8FnutqbPYjyrENXBeCyS9ODtr4")

@bot.message_handler(commands=["start"])
def send_welcome(message):
	bot.reply_to(message, """
	
	**💘සාදරයෙන් පිළිගන්නවා RS SOFTWARES BOT වෙත😊**
	
	❯මෙම බොට්ගෙන් ඔබට අපගේ නවතම මෘදුකාංග සමූහය තුළදී ලබාගත හැක.මෙම නව බොට්වරයා නිර්මාණය කලේ අපගෙ Aelita බොට්වරයාට සමූහ තුළ ක්‍රියාත්මක වීමට නොහැකි නිසයි❮
	
	🌍කෙසේ වුවත් aelita බොට්වරයාද ඔබට නොමිලේ භාවිතා කල හැක.මෙම බොට්වරයා මේ දිනවල අලුත්වැඩියා කරන බැවින් command ලබාදීමට උත්සාහ නොකරන්න.ඔබ ලබා දුන්නද එම නියෝගය ක්‍රියාත්මක නොවේ🌍
	
	commands සදහා /menu ලෙස එවන්න...
	
	🚩Owner : Ranuja Sanmira
	🚩Copyright ©2022 RS45 Crew
	🚩මෙම බොට්වරයා වෙනත් සමූහ සදහා භාවිතා නොකරන්න.
	
	""")

@bot.message_handler(commands=["how"])
def send_message(message):
	bot.reply_to(message, "**Visit our official youtube channel.**")
	
@bot.message_handler(commands=["menu"])
def send_message(message):
	bot.reply_to(message, """
	
	**꧁༺Welcome to the RS Softwares Bot V2.3༻꧂**
	
	🏁/start : start me.
	🏁/menu : get this commands message.
	🏁/info : get my information.
	🏁/dwn : Link for download our softwares.
	
	
	""")
	
@bot.message_handler(commands=["info"])
def send_message(message):
	bot.reply_to(message, """
	
	**🔛Bot Information😐**
	
	❤Name : RS SOFTWARES BOT
	❤Version : V2.3
	❤Creator : Ranuja Sanmira
	❤Owner : Ranuja Sanmira
	❤Time Table : Connecting...
	❤User Name : @soft_by_rs_bot
	
	දැනට පමණක් බැංකු සහ වෙනත් නිවාඩු දිනයන්හි වසා ඇත.(මෙය ඉදිරියේදි වෙනස් විය හැක!)
	
	""")
	
@bot.message_handler(commands=["dwn"])
def send_message(message):
	bot.reply_to(message, "**මෘදුකාංග ලබා ගැනීමේ ලින්ක් සමු නොවිය. හේතුව : ඇඩ්මින් විසින් නවතා ඇත.**")

@bot.message_handler(commands=["adminf"])
def send_message(message):
	bot.reply_to(message, """
	
	😊ඇඩ්මින් සම්බන්ධ කිරීමට @aelita_rs45_bot භාවිතා කර එහි ඇති whatsapp බටනය ඔබන්න.👍
	
	""")

bot.polling()

while True:
		pass