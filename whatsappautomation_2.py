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

    def CheckTime(tm, dt, msg):
        while True:
            if datetime.datetime.now().strftime('%H:%M') == tm and datetime.datetime.now().strftime('%d-%m-%Y') == dt:
                SendMsg(msg)
                alarmplay()
                break;

    def AddReminder(hr, mn, md, date, msg):
        main.destroy()
        print(f'Reminder created at {hr}:{mn} {md} on {date}.')
        if md == 'PM':
            if hr != '12':
                hr = str(int(hr) + 12);
        elif md == 'AM' and hr == '12':
            hr = '00'
        time_str = f'{hr}:{mn}'
        CheckTime(time_str, date, msg)

    def UpButton(limit, field, addvalue):
        value = int(field.get())
        if value + addvalue >= limit:
            field.delete(0, tk.END)
            field.insert(tk.END, str(value - limit + 1).zfill(2))
            return
        else:
            field.delete(0, tk.END)
            field.insert(tk.END, str(value + 1).zfill(2))

    def DownButton(limit, field, check_value):
        value = int(field.get())
        if value - 1 < check_value:
            field.delete(0, tk.END)
            field.insert(tk.END, limit - 1)
            return
        else:
            field.delete(0, tk.END)
            field.insert(tk.END, str(value - 1).zfill(2))

    def MeridianShift(button, field):
        if field.get() == 'AM':
            button.config(text='AM')
            field.delete(0, tk.END)
            field.insert(tk.END, 'PM')
        else:
            button.config(text='PM')
            field.delete(0, tk.END)
            field.insert(tk.END, 'AM')

    def GetDate(field):
        date_window = tk.Tk()
        date_window.title('Date Picker')
        date_window.geometry('300x250')

        cal = Calendar(date_window, selectmode='day')
        cal.config(date_pattern='dd-mm-yyyy')
        cal.pack()

        def GrabDate(cal, field):
            field.delete(0, tk.END)
            field.insert(tk.END, cal.get_date())
            date_window.destroy()

        choose_date = tk.Button(date_window, text='Choose Date', command=lambda: GrabDate(cal, field))
        choose_date.pack()