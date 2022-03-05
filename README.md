# LogFwdr
Go through the Code and Change it as appropriate. 

### INTRODUCTION
This python script allows you to specify the server, logtype and eventID. The specified logs will be forwarder to you via email. 
This script can be automated by the use of Powershell and/or Windows Task Scheduler. The interval between the sending if the logs can also be changed.
I wrote it to help me keep track of failed log in attempts of a certain system over a specific period of time. This program can also be used to monitor any type of logs.

### PREREQUISITS
1. `Python`
2. `Pip` (to install libraries)

### NOTES
1. Run with admin privileges in order to view logs
2. Use "localhost" as server to get logs from your local machine

### Changing EVENTID/COLLECTION PERIOD
```for event in events:
                #if statement allows you to filter EventIDs and duration.
                if event.EventID == 4625 or 4611 or 4634 or 4673 and now.hour - event.TimeGenerated.hour <= 24:
  ```
The if statement enables you to specify the desired EVENTID and the period in hours. The period can also be measured interms of minutes, days, months and years

### Changing the mailing parameters
```SERVER = 'smtp server' #enter smtp server
PORT = 587
FROM = 'senders email address'   #enter senders address
TO = 'recipients email address'  #enter recipients address
PASS = '' #senders email address password, make sure 2-FA is off
   ```
 Enter the specified details as strings
 
 
                
