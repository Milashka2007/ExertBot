import logging
from telebot import types
import time
import telebot
token='6360209192:AAEn4k_7BoDPTVXclLOFGaaHcp3u46yRWSA'
bot = telebot.TeleBot('6360209192:AAEn4k_7BoDPTVXclLOFGaaHcp3u46yRWSA')
orig='https://avatars.dzeninfra.ru/get-zen_doc/9196493/pub_64344c226e48e5014ccf8e26_643864ac0032a05d5a1062ab/scale_1200'
size='https://img1.teletype.in/files/00/7c/007cffec-32fa-4296-a7b4-bfe222a5e565.png'
prise='https://avatars.mds.yandex.net/get-images-cbir/1536908/mauxXGhQc5VE4Hi8Fnx5nA4867/ocr'


@bot.message_handler(commands=['start', 'Меню'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(text='Прайс лист')
    item2 = types.KeyboardButton(text='Часто задаваемые вопросы')
    item3 = types.KeyboardButton(text='О нас')
    item4 = types.KeyboardButton(text='Оформить заказ')
    item5 = types.KeyboardButton(text='Админ')
    markup.add(item1, item2, item3,item4, item5)
    bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name} , это меню канала', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def answer(call):
    if call.text == 'Админ':
        if call.from_user.id==916539100 or call.from_user.id==6830329829:
            markup1=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton(text='Ответить на вопросы')
            item2 = types.KeyboardButton(text='Меню')
            markup1.add(item1,item2)
            g=bot.send_message(call.chat.id,'Это меню админа',reply_markup=markup1)
            bot.register_next_step_handler(g,answers)
        else:
            bot.send_message(call.chat.id, 'Вы не являетесь администратором')
    if call.text=='Прайс лист':
            bot.send_photo(call.chat.id, photo=prise, caption='Наша команда выкупает товар по одному из ценников. Эти ценники означают цену за сроки обработки заказа на складе Poizon\n'
                                                              '\n'
                                                              'Тарифы:\n'
                '1) От 2000р - 20000р взимается 15%(<20001р доступно 2 лота на заказ с 50% предоплатой)\n'
                '2) От 20001р - 30000р взимается 3900р\n'
                '3) От 30001р - 40000р взимается 4700р\n'
                '4) От 40001р - 50000р взимается 5000р\n'
                '5) От 50001р - ... сумму уточнять\n'
                '(>20001р - предоплата 100%)\n'
                '\n'
                'Доставка:\n'
                '1) Доставка 12-15 дней (Оплата доставки осуществляется после взвешивания)\n'
                '2) Фото отчет за наш счет, он может задержать товар на 1 день\n'
                '\n'
                'Реферальная система:\n'
                'Что дает 2 приведенных клиента, совершивших заказ?\n'
                '\n'
                'Вы получаете возможность оформить 1 заказ без взимания процента за наши услуги')
    if call.text == 'О нас':
            bot.send_message(call.chat.id, 'Давайте знакомиться. \n'
            '\n'
            'С российского рынка ушли многие мировые фирмы по производству одежды, обуви и аксессуаров. Теперь, чтобы приобрести брендовую сумку, дизайнерские очки или любимые кроссовки, российским фанатам уличной моды осталось только два варианта: обращаться к байерам или покупать товары с рук.\n'
            '\n'
            'Однако появилась альтернатива в виде платформы Poizon. Она ориентирована исключительно на китайский рынок.\n'
            '\n'
            'Это не магазин, не ретейлер и не официальный представитель каких-либо брендов. Это международный маркетплейс, специализирующийся на продаже оригинальных брендовых товаров. \n'
            '\n'
            'Poizon - торговая площадка, которая связывает покупателя и продавца, а также обеспечивает прозрачность их сделки.\n'
            '\n'
            'Мы, Poizonswift, хотим предоставить вам свои услуги, а именно:\n'
            'возьмем на себя все необходимые шаги, чтобы выкупить товар и доставить его, поможем с проверкой подлинности товаров и обеспечим защиту ваших прав как покупателя.')
    if call.text == 'Часто задаваемые вопросы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton(text='1')
        item2 = types.KeyboardButton(text='2')
        item3 = types.KeyboardButton(text='3')
        item4 = types.KeyboardButton(text='4')
        item5 = types.KeyboardButton(text='5')
        item6 = types.KeyboardButton(text='6')
        item7 = types.KeyboardButton(text='7')
        item8 = types.KeyboardButton(text='8')
        item9 = types.KeyboardButton(text='/Меню')
        item10 = types.KeyboardButton(text='Другой вопрос')
        markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10)
        bot.send_message(call.chat.id, 'Напишите цифру интересующего вас вопроса', reply_markup=markup)
        bot.send_message(call.chat.id, '1. Что такое Poizon?')
        bot.send_message(call.chat.id, '2. На Poizon продается оригинал?')
        bot.send_message(call.chat.id, '3. Как подобрать размер обуви/одежды?')
        bot.send_message(call.chat.id, '4. Как скачать Poizon?')
        bot.send_message(call.chat.id, '5. Возможно ли привезти технику с Poizon?')
        bot.send_message(call.chat.id, '6. Что делать, если не подошел размер?')
        bot.send_message(call.chat.id, '7. Как зарегистрироваться на Poizon?')
        bot.send_message(call.chat.id, '8. Какие гарантии предоставляет сервис “Poizonswift”?')
    if call.text == 'Оформить заказ':
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Оформить заказ', url='https://t.me/swiftorder')
        markup.add(btn_my_site)
        bot.send_message(call.chat.id, "Напишите нашему администратору для заказа", reply_markup=markup)
    if call.text == '1':
        bot.send_message(call.chat.id, 'Poizon появился в 2015 году как онлайн-сообщество коллекционеров кроссовок и ценителей уличной моды. К 2022 году он смог развиться до полноценной платформы-маркетплейса брендовых и лимитированных вещей. Здесь можно купить кроссовки, одежду, сумки и аксессуары, фигурки, косметику, парфюмерию и даже электронику. Выбор настолько широк, что найти можно почти все. Poizon сотрудничает со многими партнерами на территории КНР, сюда входят как реселлеры, так и сами производители всемирных брендов, такие как Nike, Adidas, Puma, New Balance и многие другие. Их список часто обновляется, и можно найти практически все, что угодно. Можно сказать, что Poizon открывает нам весь мир одежды и обуви. В России такого ассортимента просто никогда не было! Маркетплейс работает для китайского рынка, поэтому доставить товары в Россию далеко не просто.')
    if call.text == '2':
        bot.send_photo(call.chat.id, photo=orig, caption='Poizon имеет широкий штат специалистов, которые хорошо разбираются в подлинности поставляемой продукции. Каждый представитель проходит тщательный отбор, чтобы присоединиться к команде. Все участники понимают, что невыполнение требований может привести к увольнению и штрафам. Специалисты проводят детальную проверку товаров, сертифицируют и упаковывают их перед доставкой покупателям. Poizon использует многоэтапную систему верификации и стремится сохранить свою репутацию. Перед отправкой товары проверяют на подлинность в лаборатории, их опломбировывают фирменной клипсой.')
    if call.text == '3':
        bot.send_photo(call.chat.id, photo=size, caption='B Poizon на каждый товар идёт индивидуальная размерная таблица.\n'                                                              'Вы можете подобрать себе верный размер, ориентируясь на нее.')
    if call.text == '4':
        bot.send_message(call.chat.id, 'Ссылка для Apple: https://clck.ru/rwrzo\n'
                                           '\n'
                                            'Ссылка для Android: https://clck.ru/32iBeU\n')
    if call.text == '5':
        bot.send_message(call.chat.id, 'Да, привезем любую технику. Для расчета стоимости напишите нашему менеджеру. Стоимость доставки будет зависеть от размера выбранного товара.')
    if call.text == '6':
        bot.send_message(call.chat.id, 'Возврат средств не осуществляется, если пара пришла в полном соответствии с оформленным заказом.\n'
                       'Если администратор допустил ошибку в размере или модели при заказе, то возврат происходит в течение 30 дней, после обращения.')
    if call.text == '7':
        bot.send_message(call.chat.id, '1. Первое, что вам нужно сделать, это скачать оригинальное приложение Poizon, перейдя по ссылкам для скачивания Poizon в App Store и Google Play. (Смотрите в разделе: "Как скачать Poizon?")\n'
                                            '2. При регистрации аккаунта, измените регион, нажав на +86, и поменяйте на регион +7 (Россия).\n'
                                            '3. Вам необходимо ввести свой номер телефона в поле для ввода, затем вы получите код подтверждения.\n'
                                            'Важно! (Код может прийти с 3-4 раза).')
    if call.text =='8':
        bot.send_message(call.chat.id, 'В нашем телеграмм канале “Poizonswift” вы сможете найти:\n'
                                           '\n'
                                '1) Меню канала, которое находится в закрепленных сообщениях.\n'
                                           '\n'
                                '2) #report и #photo_report, по которым вы можете отследить историю заказа с момента выкупа товара, до момента получения товара в Москве. Так же вы можете сравнить все посты, с отзывами в нашем телеграмм канале “Poizonswift.feedback”')
    if call.text == 'Другой вопрос':
        sent=bot.reply_to(call, 'Напишите интересующий вас вопрос и ожидайте ответ')
        bot.register_next_step_handler(sent, review)



def review(message):
    '''user_id = message.from_user.id'''
    bot.forward_message(6830329829, from_chat_id=message.chat.id, message_id=message.id)
    bot.send_message(6830329829, message.from_user.id)
    bot.send_message(message.chat.id, 'Твое сообщение отправлено')

def msg_from_bot_1(message):
    global user_id
    user_id = message.text
    send = bot.send_message(message.chat.id, 'Введите сообщение')
    bot.register_next_step_handler(send, msg_from_bot_2)


def msg_from_bot_2(message):
    bot.send_message(user_id, '{}'.format(message.text))
    t=bot.send_message(message.chat.id, 'Сообщение отправлено')
    bot.register_next_step_handler(t,welcome)

def answers(message):
    if message.text == 'Ответить на вопросы':
        send = bot.send_message(message.chat.id, 'Введите id пользователя, которому хотите ответить')
        bot.register_next_step_handler(send, msg_from_bot_1)
    if message.text == 'Меню':
        y=bot.send_message(message.chat.id, 'Перенаправляю в обычное меню')
        bot.register_next_step_handler(y,welcome)








while True:
    try:
        bot.polling(none_stop=True, interval=2)
        break
    except telebot.apihelper.ApiException as e:
        logging.error(e)
        bot.stop_polling()
        time.sleep(3)

