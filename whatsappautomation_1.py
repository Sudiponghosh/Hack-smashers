import tkinter as tk
from os import system
try:
    from tkcalender import Calender
except ModuleNotFoundError or ImportError:
    system('python -m pip install tkcalendar')
    from tkcalendar import Calendar
import datetime
from twilio.rest import Client
try:
    from pygame import mixer
except ModuleNotFoundError or ImportError:
    system('python -m pip install pygame')
    from pygame import mixer

account_sid = 'AC3e327e43985b03d4d3457cd92717311d'
auth_token = '9bd814031154bce6c226889682fc7ecf'
client = Client(account_sid, auth_token)

def alarmplay():
    print('playing...')
    mixer.init()
    mixer.music.load('alarmtune.wav')
    mixer.music.set_volume(1.0)
    mixer.music.play(loops=10)
    end_alarm = tk.Tk()
    end_alarm.geometry('20x30')
    end_button = tk.Button(end_alarm, text='END ALARM', command=exit)
    end_button.pack()
    end_alarm.mainloop()

def SendMsg(msg):
    if msg=='':
        msg='Blank'
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=msg,
        to='whatsapp:+919775729405'
        )
    print('Note:',msg)