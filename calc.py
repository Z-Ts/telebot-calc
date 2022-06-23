from cgitb import text
from email import message
import telebot
from telebot import types 
token=''
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Комплексные числа")
    btn2 = types.KeyboardButton("Рациональные числа")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Выберите тип чисел".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Комплексные числа"):
        bot.send_message (message.chat.id, text='введите первое число')
        bot.register_next_step_handler(message, uravnenie2)
    if(message.text == "Рациональные числа"):
        bot.send_message(message.chat.id, 'Введите выражение')
        bot.register_next_step_handler(message, uravnenie)
def uravnenie(message):
    a = 0
    s = []
    s1=0
    c=[]
    k = 0
    a = message.text
    print (a, type(a))
    for i in a:
        if i!='-' and i!='+' and i!='*' and i!='/' :
            s.append(i)
            print (s, type(s))
            k = int(''.join(s))
            print (k, type(k))
            if len(c)!=0:
                if c[0] =='+':
                    s1 =s1+k
                    с=[]
                if c[0] =='-':
                    s1 =s1-k
                    с=[]
                if c[0] =='*':
                    s1 =s1*k
                    с=[]
                if c[0] =='/':
                    s1 =s1/k
                    с=[]
                
            if len(c)==0:
                s1 = k           
        if i=='+' or i == '-' or i!='*' or i!='/':
            print (i)
            s=[]
            c=[]
    
            c.append(i)
    print (s1,'s1')
    bot.send_message(message.chat.id,text=s1)

def uravnenie2(message):
    global a1
    global a2
    global b1
    global b2
    
    a1=0
    a2=0
    b1=0
    b2=0
    a3=0
    
    a1  =message.text
    a2 = complex (a1)
    print (a2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("+")
    btn2 = types.KeyboardButton("-")
    btn3 = types.KeyboardButton("*")
    btn4 = types.KeyboardButton("/")
    markup.add(btn1, btn2,btn3, btn4)
    print(a3,'!')
    bot.send_message(message.chat.id, text="Выберите оператор".format(message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, op)
@bot.message_handler(content_types=['text'])
def op(message):
    global a3
    a3 = message.text
    bot.send_message(message.chat.id, a3, reply_markup=types.ReplyKeyboardRemove())
            
    print(a3,'a3')
    
    bot.send_message (message.chat.id, text='введите второе число')
    bot.register_next_step_handler(message, ch2)
@bot.message_handler(content_types=['text'])
def ch2(message):
    b1  =message.text
    b2 = complex (b1)
    print (b2)
    print(a2,b2,a3)    
    res = 0
    if a3 == '*':
        res = a2*b2
    elif a3 == '/':
        res = a2/b2
    elif a3 == '+':
        res = a2+b2
    elif a3 == '-':
        res = a2-b2

    print (res)
    bot.send_message(message.chat.id,text= res)     
    
    
    
bot.polling(none_stop=True)