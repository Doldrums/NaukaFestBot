#!/usr/bin/rus python
# -*- coding: utf-8 -*-
from telegram.ext import Updater, InlineQueryHandler, CommandHandler,  MessageHandler, Filters
import requests
import re


answer_list = [
	 'START49',
	 '7Z5WE64R9L8FQ107758S',
	 'C50LQEZJLHN5TRJBNO9K',
	 'F906B6KC7A2TY1YLYJ95',
	 'EGLP0MRAWH4RP8ORIIN0',
	 'MGJY0SCHPXU6I5AZ2G7V',
	 'GFGAZ2IRBYQZ3O37415H',
	 'R114QZQ4G8MLW6BQJX6E',
	 'MI8FI2GB46XAXWO02W4C',
	 'LQ50CW74L7B332J8K3B',
	 'XG98ETIW2XWBZJBKER1L'
	] 
user_list = []
progress_list = []

########Получение собачки############
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    print("Хороший мальчик получен.. ")
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def getBoy(bot, update):
	print("Запрос на получение хорошего мальчика.. ")
	url = get_image_url()
	print(update.message)
	chat_id = update.message.chat_id
	update.message.reply_text('Вот собачка для тебя! Удачи в прохождении квеста)')
	bot.send_photo(chat_id=chat_id, photo=url)


############### Получение дополнительной информации по правилам ##################
def help(bot, update):
	print("Запрос на получение правил игры.. ")
	print(update.message)
	update.message.reply_text('👋🤖Привет, я квест-бот 49 лицея!')
	update.message.reply_text('Сейчас я расскажу обо всех моментах мероприятия, но если у тебя еще останутся какие-либо вопросы, например по заданиям, ты всегда можешь постучать в лс к моим создателям за подсказкой (они для всех одинаковы)   Ссылку на их контакты найдешь ниже :) ')
	update.message.reply_text('💬Правила:')
	update.message.reply_text('По всей территории школы развешаны листовки с кодом. Первые пять человек, которые смогут собрать все данные, опередив остальных, получат сладкие призы. Возможно объединяться в команды, но состоящие не более чем из пяти человек. Чтобы найти код придется проявить смекалку и умение ориентироваться в школе, ведь узнавать о местонахождении заветного ключа получится с помощью ассоциаций между ответом к заданию и конкретной локацией. Помогут даже мельчайшие детали.')
	update.message.reply_text('🧭Тайминг:')
	update.message.reply_text('На прохождение квеста отведено достаточно много времени, и я буду работать до конца фестиваля науки. Однако победители определятся уже в первые дни в зависимости от скорости выполнения заданий.')
	update.message.reply_text('❗ВАЖНО:')
	update.message.reply_text('Мы советуем скринить ваш прогресс, ибо если бот упадет, мы не гарантируем полный возврат статистики. А также мы никак не тестировали бота, и надеимся что вы не будете его специально ломать. Все коды находятся на видных местах, в кабинеты заходить не нужно)')
	update.message.reply_text('💯Как победить:')
	update.message.reply_text('Квест стартует для всех одновременно. Чтобы получить первую задачу, напиши START49. Как только получишь ответ и догадаешься, где спрятан код, отправляй ключ с листовки мне, чтобы перейти к следующему заданию.')
	update.message.reply_text('👥Контакты моих создателей:')
	update.message.reply_text('Эмма 10В vk: /lundenceaster, tg: @lundenkust')
	update.message.reply_text('Орина 10И vk: /dravsrvuite, tg: @doldrums3')
	print('Правила игры получены..')
###############################Получение заданий####################

def get_task(i):
	tast_list = [
	 'https://imgur.com/mPMh8sl',
	 'https://imgur.com/EQwZE4L',
	 'https://imgur.com/li4V7FG',
	 'https://imgur.com/6n3eahm',
	 'https://imgur.com/HgGwhDT',
	 'https://imgur.com/J7KZrXL',
	 'https://imgur.com/qSntmgi',
	 'https://imgur.com/i3mbjm1',
	 'https://imgur.com/gOy35Kd',
	 'https://imgur.com/gPkTVK3']
	current_task = tast_list[i]
	print("Текущее задание получено..")
	return current_task

def gettask(bot, update, i):
	print("Запрос на получение задания.. ")
	print(update.message)
	url = get_task(i)
	chat_id = update.message.chat_id
	update.message.reply_text('Текущее задание:')
	bot.send_photo(chat_id=chat_id, photo=url)
	
def check(bot, update):
	print('проверяю..')
	print(update.message.text)
	print(user_list)
	print(progress_list)
	i = progress_list[user_list.index(update.message.chat.username)]
	if (i==10):
		print('ОМГ ПОБЕДИТЕЕЕЛЬЬЬЬЬЬЬ', update.message.chat.username)
		update.message.reply_text('🔥👍💯💥УРА! Ты прошел квест до конца! Поздравляю, ожидай подведения итогов :)')
	else:
		print(i)
		if (update.message.text == answer_list[i]):
				update.message.reply_text('🔥Агонь! Всё верно, получай следующее задание..')
				progress_list[user_list.index(update.message.chat.username)] = i+1
				gettask(bot, update, i)
		else:
				update.message.reply_text('⁉Стоит подумать ещё')

def start(bot, update):
	print('Бот запущен новым участником..')
	print(update.message)
	user_list.append(update.message.chat.username)
	progress_list.append(0)
	print('Высылаю правила квеста..')
	update.message.reply_text('Напиши /help !)')
	print('Правила высланы..')


def main():
    updater = Updater('891634829:AAGzET5HwtdMpcSdIp4qCWoWHIq7tuQNXWc')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('guy',getBoy))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('task',gettask))
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(MessageHandler(Filters.text, check))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
	main()