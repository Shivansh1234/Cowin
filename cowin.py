import json
import requests
from datetime import date, timedelta, datetime
from plyer import notification
import schedule
import time

print('script started and running...')

def cowin():
    arr = []
    k = []
    for x in range(0, 11):
        pincode = '282002'
        somedate = date.today() + timedelta(days=x)
        change = somedate.strftime('%d-%m-%Y')
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" +pincode+ "&date=" + change
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        r = requests.get(url, headers=headers).content.decode()
        r = json.loads(r)
        arr.append(r)

    for x in arr:
        k+= x['centers']

    for x in k:
        if x['sessions'][0]['available_capacity'] > 0:
            print('Hospital Name','\t\t\t\t', 'Session Date','\t\t\t\t', 'Available Capacity')
            print(x['name'],'\t\t\t\t', x['sessions'][0]['date'],'\t\t\t\t', x['sessions'][0]['available_capacity'])
            notification.notify(title="Hi Shivansh!", message="Vaccines are available", timeout=10)
            break;

cowin()
schedule.every(1).minute.do(cowin)

while True:
  schedule.run_pending()
