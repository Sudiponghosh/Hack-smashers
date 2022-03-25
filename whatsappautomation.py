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

def CheckTime(tm,dt,msg):
    while True:
        if datetime.datetime.now().strftime('%H:%M')==tm and datetime.datetime.now().strftime('%d-%m-%Y')==dt:
            SendMsg(msg)
            alarmplay()
            break;

def AddReminder(hr,mn,md,date,msg):
    main.destroy()
    print(f'Reminder created at {hr}:{mn} {md} on {date}.')
    if md=='PM':
        if hr!='12':
            hr=str(int(hr)+12);
    elif md=='AM' and hr=='12':
        hr='00'
    time_str=f'{hr}:{mn}'
    CheckTime(time_str,date,msg)

def UpButton(limit,field,addvalue):
    value=int(field.get())
    if value+addvalue>=limit:
        field.delete(0, tk.END)
        field.insert(tk.END, str(value-limit+1).zfill(2))
        return
    else:
        field.delete(0,tk.END)
        field.insert(tk.END,str(value+1).zfill(2))

def DownButton(limit,field,check_value):
    value=int(field.get())
    if value-1<check_value:
        field.delete(0, tk.END)
        field.insert(tk.END,limit-1)
        return
    else:
        field.delete(0,tk.END)
        field.insert(tk.END,str(value-1).zfill(2))

def MeridianShift(button,field):
    if field.get()=='AM':
        button.config(text='AM')
        field.delete(0, tk.END)
        field.insert(tk.END,'PM')
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

    def GrabDate(cal,field):
        field.delete(0,tk.END)
        field.insert(tk.END,cal.get_date())
        date_window.destroy()

    choose_date=tk.Button(date_window,text='Choose Date',command= lambda : GrabDate(cal,field))
    choose_date.pack()

main=tk.Tk()
main.geometry('200x300')
main.title("Work planar")
tk.Label(text='Add Work',fg='Blue',font=('Ariel',12)).pack()
timepanel=tk.Frame(main)
timepanel.pack(pady=5)

up_img=tk.PhotoImage(file="up.png")
down_img=tk.PhotoImage(file="down.png")

hour=tk.Entry(timepanel,width=2,font=(16))
hour.insert(tk.END,'12')
hour.grid(row=1,column=0,padx=5)

tk.Label(timepanel,text=':').grid(row=1,column=1)

min=tk.Entry(timepanel,width=2,font=(16))
min.insert(tk.END,'00')
min.grid(row=1,column=2,padx=5)

meridian_segment=tk.Entry(timepanel,width=3,font=(16))
meridian_segment.insert(tk.END,'AM')
meridian_segment.grid(row=1,column=3,padx=5)

hour_up=tk.Button(timepanel,image=up_img,height=10,width=13,command=lambda : UpButton(12,hour,0))
hour_up.grid(row=0,column=0)
hour_down=tk.Button(timepanel,image=down_img,height=10,width=13, command=lambda : DownButton(13,hour,1))
hour_down.grid(row=2,column=0)

min_up=tk.Button(timepanel,image=up_img,height=10,width=13,command=lambda : UpButton(60,min,1))
min_up.grid(row=0,column=2)
min_down=tk.Button(timepanel,image=down_img,height=10,width=13, command=lambda : DownButton(60,min,0))
min_down.grid(row=2,column=2)

meridian_switch=tk.Button(timepanel,text='PM',command=lambda : MeridianShift(meridian_switch,meridian_segment))
meridian_switch.grid(row=1,column=4)

date=tk.Entry(main,width=10)
date.pack()

date_button=tk.Button(main,text='Set Date',command= lambda : GetDate(date))
date_button.pack()

tk.Label(text='Note:').pack()
note=tk.Text(main,height=3,width=20)
note.pack(pady=3)

add_reminder=tk.Button(main,text='Add Reminder',font=('Ariel','12'),bg='Blue',fg='White',command=lambda : AddReminder(hour.get(),min.get(),meridian_segment.get(),date.get(),note.get(1.0,'end-1c')))
add_reminder.pack()
main.mainloop()