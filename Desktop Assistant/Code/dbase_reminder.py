import sqlite3 
import datetime
import file as f
#import dbase_reminder as r
import  nancy as n


dbase = sqlite3.connect('d_reminder.db')
print ('new data base')
dbase.execute('''create table if not exists empolyee_records(DATE TEXT NOT NULL,TIME TEXT , EVENT TEXT NOT NULL)''')
print('table entered')

def insert_record(DATE,TIME,EVENT):
    dbase.execute('''insert into empolyee_records (DATE,TIME,EVENT)
                  VALUES(?,?,?)''',(DATE,TIME,EVENT))
    dbase.commit()


'''def call(DATE,TIME,EVENT):
    insert_record((DATE,TIME,EVENT)
    print('call')
'''


def read_data():
    data = dbase.execute('''SELECT DATE ,TIME, EVENT  FROM empolyee_records  ''')
    for record in data :
        print('date: ' +str(record[0]) + '\n')
        print('time: ' +str(record[1]) + '\n')
        print('event: ' +str(record[2]) + '\n')




print('table close')

def reminder():
    n.speak('what is your reminder ')
    rem=n.Take_Command()
    print(rem)
    n.speak('ok tell the date when i remind you')
    time=n.Take_Command()
    insert_record(datetime.date.today(),datetime.time(), rem)  
    print('enter in database')   

    if 'today' in time:
        tday = datetime.date.today() 
        if tday == datetime.date.today():
           return f.reminders(rem)
    elif 'tomorrow' in time:
        tday = datetime.date.today()
        tdelta = datetime.timedelta(days=1)
        date = tday + tdelta
        if date == datetime.date.today():
             return f.reminders(rem) 
         
reminder()
read_data()
dbase.close()