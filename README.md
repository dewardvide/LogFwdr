# LogFwdr
Go through the Code and Change it as appropriate. 

### INTRODUCTION
This python script allows you to specify the server, logtype and eventID. The specified logs will be forwarder to you via email. 
This script can be automated by the use of Powershell and/or Windows Task Scheduler. The interval between the sending if the logs can also be changed.
I wrote it to help me keep track of failed log in attempts of a certain system over a specific period of time. 

### PREREQUISITS
1. `Python`
2. `Pip` (to install libraries)
3. Libraries:
    * `win32evtlog`
    * `datetime`
    * `smtplib`
    * `datetime`

### NOTES
1. Run with admin privileges in order to view logs
2. Use "localhost" as server to get logs from your local machine
