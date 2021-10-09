import smtplib
import json
import requests
import sys

conn=smtplib.SMTP('smtp.office365.com',587) # SMTPServer, Port
conn.ehlo() # connect to SMTP server
conn.starttls() #begin encryption
password=input('Enter email password:\n')
conn.login('ENTER YOUR EMAIL ADDRESS HERE', f"{password}")

APPID='ENTER APP ID HERE'
location="lat=52.51&lon=13.50"
url=f'https://api.openweathermap.org/data/2.5/onecall?{location}&appid={APPID}&units=metric'
response=requests.get(url)
response.raise_for_status()
w=json.loads(response.text)

body=('---Current Weather---\n'
'Feels like ' +str(w['current']['feels_like'])+' degrees.\n'
'The temperature is '+str(w['current']['temp'])+' degrees.\n'
+str(w['current']['weather'][0]['description'])+'.\n')

outlooks=[]

for i in range(3):

    outlook=('In '+str(i+1)+' h it will feel like '
          + str(w['hourly'][i]['feels_like'])+' degrees and we can expect '
          + str(w['hourly'][i]['weather'][0]['description']+'.'))
    outlooks.append(outlook)
    
outlookslist='\n'.join([str(entry) for entry in outlooks])

conn.sendmail('YOUR EMAIL ADDRESS HERE', 'RECIPIENT ADDRESS HERE',
              f"Subject: The Weather \n\n{body}\n\n ---Outlook---\n{outlookslist}")
              
              
conn.quit() # quit connection to SMTP server
