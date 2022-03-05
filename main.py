import win32evtlog
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


now = datetime.datetime.now()

server = "localhost"
logtype = 'Security'
hand = win32evtlog.OpenEventLog(server, logtype)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(hand)

Sec_logs = ''

def get_events():
    while True:
        events = win32evtlog.ReadEventLog(hand, flags,0)
        if events:
            for event in events:
                #if statement allows you to filter EventIDs and duration.
                if event.EventID == 4625 or 4611 or 4634 or 4673 and now.hour - event.TimeGenerated.hour <= 24:
                    Sec_logs = [event.EventID, event.EventCategory, event.EventType, event.SourceName, event.TimeGenerated.hour, event.TimeGenerated.minute, event.TimeGenerated.second]
            return(Sec_logs)

logs =  str(get_events())

print('Composing Email...')

SERVER = 'smtp server' #enter smtp server
PORT = 587
FROM = 'senders email address'   #enter senders address
TO = 'recipients email address'  #enter recipients address
PASS = '' #senders email address password, make sure 2-FA is off

msg = MIMEMultipart()

msg['Subject'] = 'Security Logs. Date: '+''+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['from'] = FROM
msg['To'] = TO

msg.attach(MIMEText(logs, 'html'))

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()

server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent')

server.quit()



